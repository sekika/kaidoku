$.ajax({
    url:'https://raw.githubusercontent.com/sekika/kaidoku/master/kaidoku/data/sudoku.txt',
	beforeSend: function(){
       $('#board').html(boardhtml(Array(9+1).join('Loading..')));
	},
    success: function(data){
        level = localStorage.getItem("level");
        if (level == null) {
            level = 3
            localStorage.setItem("level", level);
        }
        no = localStorage.getItem("level"+level);
        if (no == null) {
            no = 1;
            s = sudoku(data, level, no);
            localStorage.setItem("s"+level, s);
        } else {
            s = localStorage.getItem("s"+level);
            if (s == null || s.length < 81) {
                s = sudoku(data, level, no);
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
            no+"' onkeyup='updatenum()'>"
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
            s = sudoku(data, level, no);
            localStorage.setItem("s"+level, s);
        } else {
            document.getElementById("no").value = no;
            s = localStorage.getItem("s"+level);
            if (s == null || s.length < 81) {
                s = sudoku(data, level, no);
            }
        }
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
           localStorage.setItem("level"+level, no);
           s = sudoku(data, level, no);
           localStorage.setItem("s"+level, s);
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
    if (activecell != '') {
        document.getElementById(activecell).className = 'internal';
        content = document.getElementById(activecell).innerHTML;
        content = content.replace(/<("[^"]*"|'[^']*'|[^'">])*>/g,'');
        if ( content.length == 1 ) {
            c = "cell";
        } else {
            c = "mark";
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
    if (activecell.length == 0) {
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
            mark = content.slice(0, 3);
            i = 1;
            while ( i*3 < mark.length ) {
                mark += content.slice(i * 3 + 1, i*3 + 3);
            }
        } else {
            if (  content.length % 4 == 3 ) {
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
    if (numblank(s) > 0) {
        // Solved
        start = localStorage.getItem("s"+level);
        document.getElementById(activecell).className = 'internal';
        for ( i = 0; i < 81; i++ ) {
            if (start[i] == 0) {
                num = "<div class='blue'>"+s[i]+"</div>";
            } else {
                num = s[i];
            }
            document.getElementById(i).innerHTML = num;
        }
        document.getElementById("activecell").textContent = 'solved';
    }
};

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
   if ( activecell == 'solved' ) {
       return;
   }
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

function keydown(key){
     keycode = key.keyCode;
     // numeric key
     if ( keycode > 48 && keycode < 58 ) {
         num(keycode - 48);
     }
     // backspace or delete key
     if ( keycode == 8 || keycode == 46 ) {
         num(0);
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

function sudoku(data, level, no) {
var lines = data.split("\n");
n = 0
for (var i = 0; i < lines.length; i++) {
   line = lines[i].split(" ");
   if (line[0] == level) {
       n++
       s = line[1]
       if (n >= no) {
           i = lines.length
       }
   }
}
    return s;
}

function boardhtml(s) {

var board = "<table class='external'>"
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
return board;
}
