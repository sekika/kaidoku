$.ajax({
    url:'https://raw.githubusercontent.com/sekika/kaidoku/master/kaidoku/data/sudoku.txt',
    success: function(data){
        board = boardhtml(Array(9+1).join('Loading..'));
        document.getElementById("board").innerHTML = board;
        level = localStorage.getItem("level");
        if (level == null) {
            level = 3
            localStorage.setItem("level", level);
        }
        no = localStorage.getItem("level"+level);
        if (no == null) {
            no = 1;
            [s, last] = sudoku(data, level, no);
            localStorage.setItem("s"+level, s);
        } else {
            s = localStorage.getItem("s"+level);
            last = localStorage.getItem("last"+level);
            if (s == null || last == null || s.length < 81) {
               [s, last] = sudoku(data, level, no);
               if (no > last) {
                    document.getElementById("no").textContent = last;
               }
               localStorage.setItem("s"+level, s);
            }
        }
        document.getElementById("current").textContent = s;
        lang = document.getElementById("lang").textContent;
        if ( lang == 'ja' ) {
            levelname = ['レベル', '簡単すぎ', '超簡単', '簡単', '普通', '難しい', 'とても難しい', '意地悪', '難しすぎ', '究極'];
            noname = '問題番号';
        } else {
            levelname = ['Level ', 'trivial', 'very easy', 'easy', 'normal', 'hard', 'very hard', 'evil', 'extreme', 'ultimate'];
            noname = 'No.';
        }
        problem = "<select id='level' onChange='updatelevel()'>"
        for (var i = 1; i <= 9; i++) {
            problem += "<option value='"+i+"'";
            if (i == level) {
                problem += " selected";
            }
            problem += ">" + levelname[0] +i+": ";
            problem += levelname[i];
            problem += "</option>";
        }
        problem += "</select>\n";
        problem += noname + " <input type='text' name='no' id='no' size='5' maxlength='5' value='" +
            no+"' onkeyup='updatenum()'>";
        problem += " / " + "<span id='last'>" + last + "</span>";
        $('#problem').html(problem);
        board = boardhtml(s);
        $('#board').html(board);
        $('#data').text(data);
        clear();
    },
    error: function () {
        $('#board').html('Could not load sudoku problems.');
    }
});

// Change the level
function updatelevel() {
       data = document.getElementById("data").textContent;
       level = document.getElementById("level").value;
       localStorage.setItem("level", level);
       no = localStorage.getItem("level"+level);
       if (no == null) {
            no = 1;
            document.getElementById("no").value = no;
            [s, last] = sudoku(data, level, no);
            if (no > last) {
                document.getElementById("no").textContent = last;
            }
            localStorage.setItem("s"+level, s);
        } else {
            document.getElementById("no").value = no;
            s = localStorage.getItem("s"+level);
            last = localStorage.getItem("last"+level);
            if (s == null || last == null || s.length < 81) {
                [s, last] = sudoku(data, level, no);
                if (no > last) {
                    document.getElementById("no").textContent = last;
                }
            }
        }
        localStorage.setItem("last"+level, last);
        document.getElementById("last").textContent = last;
        document.getElementById("current").textContent = s;
        board = boardhtml(s)
        $('#board').html(board);
        clear();
};

// Change the problem number
function updatenum() {
       data = document.getElementById("data").textContent
       level = document.getElementById("level").value
       no = document.getElementById("no").value
       if (isFinite(no) && no>"") {
           localStorage.setItem("level", level);
           [s, last] = sudoku(data, level, no);
           if (no > last) {
               no = last;
               document.getElementById("no").textContent = last;
           }
           localStorage.setItem("level"+level, no);
           localStorage.setItem("s"+level, s);
           localStorage.setItem("last"+level, last);
           document.getElementById("last").textContent = last;
           document.getElementById("current").textContent = s;
           board = boardhtml(s)
           $('#board').html(board);
           clear();
       }
};

function clear() {
     $('#message').text('');
     $('#activecell').text('');
}

function numblank(s) {
    blank = 0;
    for (var i = 0; i < 81; i++) {
        if (s[i] == 0) {
            blank ++;
        }
    }
    return blank;
};

// Click a cell
function btn(i) {
    activecell = document.getElementById("activecell").textContent;
    if ( activecell == 'solved' ) {
        return;
    }
    if (activecell != '') {
        document.getElementById(activecell).className = 'internal';
        content = document.getElementById(activecell).innerHTML;
        content = content.replace(/<("[^"]*"|'[^']*'|[^'">])*>/g,'');
        if ( content.length == 1 ) {
            c = "cell";
        } else {
            if ( content.length > 3 ) {
                c = "mark";
            } else {
                c = "mark3";
            }
        }
         $('#'+activecell).html("<button type='button' class='"+c+"' id='b"+
            activecell+"' onClick='btn("+activecell+")'>"+content+"</button>");
    }
    content = document.getElementById(i).innerHTML;
    n = content.replace(/<("[^"]*"|'[^']*'|[^'">])*>/g,'');
    document.getElementById(i).textContent = n;
    if ( n.length == 1 ) {
        document.getElementById(i).className = 'selected';
    } else {
        document.getElementById(i).className = 'selectedmark';
    }
    document.getElementById("activecell").textContent = i;
};

// Place a number
function num(n) {
    activecell = document.getElementById("activecell").textContent;
    if (activecell.length == 0 || activecell == 'solved') {
        return;
    }
    s = document.getElementById("current").textContent;

    content = document.getElementById(activecell).innerHTML;
    content = content.replace(/<("[^"]*"|'[^']*'|[^'">])*>/g,'');
    // Check if available
    if ( n-0 != 0 && !content.includes(n) ) {
        match = scancell(s, n);
        if ( match.length > 0 ) {
            highlight(match);
            return;
        }
    }
    // Pencil mark ?
    if (content != ' ' && n-0 != 0) {
        if ( content.includes(n) ) {
            content = content.replace(n,'');
            while ( content.includes(' ')) {
                content = content.replace(' ','');
            }
            mark = content.slice(0, 5);
            if ( mark.length > 5 ) {
                mark += content.slice(6, 9);
            }
        } else {
            if (  content.length == 5 ) {
                content += ' ';
            }
            mark = content + '' + n;
        }
        if ( mark.length > 1 ) {
            $('#'+activecell).html("<button type='button' class='selectedmark' id='b"+
               activecell+"' onClick='btn("+activecell+")'>"+mark+"</button>");
            s = s.slice(0, activecell-81) + '0'  + s.slice(activecell-1+2);
            document.getElementById("current").textContent = s;
            return;
        }
        if ( mark.length == 1 ) {
           n = mark;
           if ( n-0 != 0) {
               match = scancell(s, n);
               if ( match.length > 0 ) {
                   highlight(match);
                   return;
               }
           }
        } else {
            n = '0';
        }
    }    
    // Put a number
    s = s.slice(0, activecell-81) + n  + s.slice(activecell-1+2);
    document.getElementById("current").textContent = s;
    if ( n-0 == 0 ) {
        n = ' '
    }
    $('#'+activecell).html("<button type='button' class='selected' id='b"+
            activecell+"' onClick='btn("+activecell+")'>"+n+"</button>");
    document.getElementById("message").innerHTML = "";
    if (numblank(s) == 0) {
        // Solved
        start = localStorage.getItem("s"+level);
        document.getElementById(activecell).className = 'internal';
        $('#'+activecell).html("<button type='button' class='cell' id='b"+
            activecell+"' onClick='btn("+activecell+")'>"+n+"</button>");
        no = document.getElementById("no").value - 0;
        last = document.getElementById("last").textContent - 0;
        if ( no < last ) {
            $('#buttons').html("<button type='button' id='next' class='next' onClick='next()'>Next</a>");
        } else {
            $('#buttons').html("");
        }
        document.getElementById("activecell").textContent = 'solved';
        showmessage({en: 'This is the solution.', ja: 'これが正解です。'});
    }
};

// Next problem
function next() {
   no = document.getElementById("no").value - 0;
   last = document.getElementById("last").textContent - 0;
   if ( no < last) {
      document.getElementById("no").value = no+1;
      updatenum();
   }
}

// Show mesage
function showmessage(message) {
    lang = document.getElementById("lang").textContent;
    if ( lang in message ) {
        message = message[lang];
    } else {
        message = message['en'];
    }
    document.getElementById("message").innerHTML = message;
}

// Scan duplicated numbers
function scancell(s, n) {
    matched = 0;
    var match = new Array();
    row = Math.floor(activecell / 9);
    column = activecell % 9;
    begin = Math.floor(row / 3) * 27 + Math.floor(column / 3)*3;
    box = [0, 1, 2, 9, 10, 11, 18, 19, 20];
    for (var i = 0; i < 9; i++) {
        if (s[begin + box[i]] == n && activecell != begin + box[i]) {
            match[matched] = begin + box[i];
            matched ++;
        }
    }
    for (var i = 0; i < 9; i++) {
        if (s[row * 9 + i] == n  && i != column) {
            match[matched] = row * 9 + i;
            matched ++;
        }
        if (s[i * 9 + column] == n && i != row) {
            match[matched] = i * 9 + column;
            matched ++;
        }
    }
    return match;
}

// Highlight the matching cells
function highlight(match) {
    for (var i = 0; i < match.length; i++) {
        document.getElementById(match[i]).innerHTML = "<div class='red'>"+s[match[i]]+"</div>";
    }
    var timeout_id = setTimeout(restorenumber , 5000);
}

// Finish highlight
function restorenumber() {
   activecell = document.getElementById("activecell").textContent;
   level = document.getElementById("level").value
   s = localStorage.getItem("s"+level);
   c = document.getElementById("current").textContent;
   for (i = 0; i < 81; i++) {
        if (c[i] != 0 && i != activecell) {
            if (s[i] == 0) {
                document.getElementById(i).innerHTML = 
                    "<button type='button' class='cell' id='b"+
                     i+"' onClick='btn("+i+")'>"+c[i]+"</button>"
            } else {
                document.getElementById(i).textContent = s[i];
            }
        }
    }
};

// Keyboard pressed
document.onkeydown = keydown;

function copyText(text){
    var ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand("copy");
    ta.parentElement.removeChild(ta);
}

function keydown(key){
     keycode = key.keyCode;
     char = String.fromCharCode(keycode);
     // numeric key
     if ( keycode > 48 && keycode < 58 ) {
         num(keycode - 48);
     }
     // backspace, delete key or x
     if ( keycode == 8 || keycode == 46 || char == "X") {
         num(0);
     }
     // c: copyt to clipboard
     if ( char == "C" ) {
         current = document.getElementById("current").textContent;
         copyText(current);
         en = "Current position<br>"+current+"<br>copied to clipboard."
         ja = "現局面は<br>"+current+"<br>クリップボードにコピーしました。"
         showmessage({en: en, ja: ja});
         return;
     }
     activecell = document.getElementById("activecell").textContent;
     level = document.getElementById("level").value;
     s = localStorage.getItem("s"+level);
     if (activecell.length == 0) {
         return;
     }
     activecell = activecell - 0;
     // left arrow
     if ( keycode == 37 ) {
         if ( activecell % 9 > 0 ) {
             do {
                 activecell -= 1;
             } while ( s[activecell] != 0 && activecell % 9 > 0 )
             if (s[activecell] == 0) {
                 btn(activecell);
             }
         }
     }
     // up arrow
     if ( keycode == 38 ) {
         if ( activecell > 8 ) {
             do {
                 activecell -= 9;
             } while ( s[activecell] != 0 && activecell > 8 )
             if (s[activecell] == 0) {
                 btn(activecell);
             }
         }
     }
     // right arrow
     if ( keycode == 39 ) {
         if ( activecell % 9 < 8 ) {
             do {
                 activecell += 1;
             } while ( s[activecell] != 0 && activecell % 9 < 8 )
             if (s[activecell] == 0) {
                 btn(activecell);
             }
         }
     }
     // down arrow
     if ( keycode == 40 ) {
         if ( activecell < 72 ) {
             do {
                 activecell += 9;
             } while ( s[activecell] != 0 && activecell < 72 )
             if (s[activecell] == 0) {
                 btn(activecell);
             }
         }
     }
};

// Read sudoku data
function sudoku(data, level, no) {
    var lines = data.split("\n");
    n = 0;
    found = false;
    for (var i = 0; i < lines.length; i++) {
       line = lines[i].split(" ");
       if (line[0] == level) {
           n++;
           if (!found) {
               s = line[1]
           }
           if (n == no) {
               found = true;
           }
       }
    }
    return [s, n];
}

// HTML of board
function boardhtml(s) {

if ( window.innerWidth > 640 ) {
   var board = "<table class='invisible'><tr class='invisible'><td class='invisible'>";
} else {
   var board = '';
}

board += "<table class='external'>"
for (var x = 0; x < 3; x++) {
    board += "<tr>";
    for (var y = 0; y < 3; y++) {
        board += "<td class='external'><table>";
        for (var i = 0; i < 3; i++) {
            board += "<tr class='internal'>";
            for (var j = 0; j < 3; j++) {
                cell = x*27+i*9+y*3+j
                if (s[cell] == 0) { 
                    board += "<td class='internal' id='"+cell+"'>"+ 
                    "<button type='button' class='cell' id='b"+cell+
                    "' onClick='btn("+cell+")'>"+' '+"</button></td>";
                } else {
                    board += "<td class='internal' id='"+cell+"'>"+s[cell]+"</td>";
                }
            }
        }
        board += "</table></td>";
    }
}
board += "</table>";

if ( window.innerWidth > 640 ) {
   board += "<td class='invisible' style='width: 20px'>";
   board += "<td id='buttons' class='invisible'>";
   w = 2;
} else {
   board += "<p></p>";
   w = 5;
}

board += "<table class='invisible'>";
for ( i = 1; i < 10; i ++ ) {
    if ( i % w == 1 ) {
        board += "<tr>";
    }
    board += "<td id='n" + i + "'><button type='button' class='command' id='bn" +
        i + "' onClick='num(" + i + ")'>" + i + "</button>";
    if ( i % w == 0 ) {
        board += "</tr>";
    }
}
board += "<td id='del'><button type='button' class='command' id='del' onClick='num(0)'>X</button>";
board += "</tr></table>";

if ( window.innerWidth > 640 ) {
    board += "</table>";
}
return board;
}
