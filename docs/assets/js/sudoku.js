"use strict";
$.ajax({
    url: 'https://raw.githubusercontent.com/sekika/kaidoku/master/kaidoku/data/sudoku.txt',
    success: function (data) {
        var level = localStorage.getItem("level");
        if (level == null) {
            level = 3;
            localStorage.setItem("level", level);
        }
        var no = localStorage.getItem("level" + level);
        if (no == null) {
            no = 1;
            [s, last] = sudoku(data, level, no);
            localStorage.setItem("s" + level, s);
        } else {
            var s = localStorage.getItem("s" + level);
            var last = localStorage.getItem("last" + level);
            if (s == null || last == null || s.length < 81) {
                [s, last] = sudoku(data, level, no);
                if (no > last) {
                    document.getElementById("no").textContent = last;
                }
                localStorage.setItem("s" + level, s);
            }
        }
        var levelname = getlevelname();
        var noname = getnoname();
        var problem = "<select id='level' onChange='updatelevel()'>";
        for (var i = 1; i <= 9; i++) {
            problem += "<option value='" + i + "'";
            if (i == level) {
                problem += " selected";
            }
            problem += ">" + levelname[0] + i + ": ";
            problem += levelname[i];
            problem += "</option>";
        }
        problem += "</select>\n";
        problem += noname + " <input type='text' name='no' id='no' size='5' maxlength='5' value='" + no +
            "' onkeyup='updatenum()'>";
        problem += " / " + "<span id='last'>" + last + "</span>";
        $('#problem').html(problem);
        $('#data').text(data);
        drawboard();
    },
    error: function () {
        $('#board').html('Could not load sudoku problems.');
    }
});
// Change the level
function updatelevel() {
    var data = document.getElementById("data").textContent;
    var level = document.getElementById("level").value;
    localStorage.setItem("level", level);
    var no = localStorage.getItem("level" + level);
    localStorage.setItem("note", '');
    if (no == null) {
        no = 1;
        document.getElementById("no").value = no;
        [s, last] = sudoku(data, level, no);
        if (no > last) {
            document.getElementById("no").textContent = last;
        }
        localStorage.setItem("s" + level, s);
    } else {
        document.getElementById("no").value = no;
        var s = localStorage.getItem("s" + level);
        var last = localStorage.getItem("last" + level);
        if (s == null || last == null || s.length < 81) {
            [s, last] = sudoku(data, level, no);
            if (no > last) {
                document.getElementById("no").textContent = last;
            }
        }
    }
    localStorage.setItem("level" + level, no);
    localStorage.setItem("last" + level, last);
    localStorage.setItem("move", '');
    document.getElementById("last").textContent = last;
    drawboard();
};
// Change the problem number
function updatenum() {
    var data = document.getElementById("data").textContent;
    var level = document.getElementById("level").value;
    var no = document.getElementById("no").value - 0;
    localStorage.setItem("note", '');
    if (isFinite(no) && no > "") {
        localStorage.setItem("level", level);
        var s, last;
        [s, last] = sudoku(data, level, no);
        if (no > last) {
            no = last;
            document.getElementById("no").value = last;
        }
        localStorage.setItem("level" + level, no);
        localStorage.setItem("s" + level, s);
        localStorage.setItem("last" + level, last);
        localStorage.setItem("move", '');
        document.getElementById("last").textContent = last;
        drawboard();
    }
};
// Click a cell
function btn(i) {
    var activecell = document.getElementById("activecell").textContent;
    if (activecell == 'solved') {
        return;
    }
    if (activecell != '') {
        deselect(activecell);
    }
    var content = document.getElementById(i).innerHTML;
    var n = content.replace(/<("[^"]*"|'[^']*'|[^'">])*>/g, '');
    document.getElementById(i).textContent = n;
    if (n.length == 1) {
        document.getElementById(i).className = 'selected';
    } else {
        document.getElementById(i).className = 'selectedmark';
    }
    document.getElementById("activecell").textContent = i;
};
// Place a number
function num(n) {
    n -= 0;
    if (n > 9) {
        n = n - 10;
        var save = false; // Avoid duplicate saving
    } else {
        var save = true;
    }
    var activecell = document.getElementById("activecell").textContent;
    if (activecell.length == 0 || activecell == 'solved') {
        return;
    }
    var s = document.getElementById("current").textContent;
    var content = document.getElementById(activecell).innerHTML;
    content = content.replace(/<("[^"]*"|'[^']*'|[^'">])*>/g, '');
    // Check if available
    if (n != 0 && !content.includes(n)) {
        var match = scancell(s, n);
        if (match.length > 0) {
            highlight(match);
            return;
        }
    }
    // Move
    if (save) {
        var move = getmove();
        move.push(activecell * 10 + n);
        savemove(move);
    }
    // Pencil mark ?
    if (content != ' ' && n - 0 != 0) {
        if (content.includes(n)) {
            content = content.replace(n, '');
            while (content.includes(' ')) {
                content = content.replace(' ', '');
            }
            var mark = content.slice(0, 5);
            if (mark.length > 5) {
                mark += content.slice(6, 9);
            }
        } else {
            if (content.length == 5) {
                content += ' ';
            }
            var mark = content + '' + n;
        }
        if (mark.length > 1) {
            $('#' + activecell).html(button(activecell, mark, 'selectedmark'));
            s = s.slice(0, activecell - 81) + '0' + s.slice(activecell - 1 + 2);
            document.getElementById("current").textContent = s;
            return;
        }
        if (mark.length == 1) {
            n = mark;
            if (n - 0 != 0) {
                match = scancell(s, n);
                if (match.length > 0) {
                    highlight(match);
                    return;
                }
            }
        } else {
            n = '0';
        }
    }
    // Put a number
    s = s.slice(0, activecell - 81) + n + s.slice(activecell - 1 + 2);
    document.getElementById("current").textContent = s;
    if (n - 0 == 0) {
        n = ' '
    }
    $('#' + activecell).html(button(activecell, n, 'selected'));
    document.getElementById("message").innerHTML = "";
    if (numblank(s) == 0) {
        // Solved
        var start = localStorage.getItem("s" + level);
        document.getElementById(activecell).className = 'internal';
        $('#' + activecell).html(button(activecell, n, 'cell'));
        var no = document.getElementById("no").value - 0;
        var last = document.getElementById("last").textContent - 0;
        if (no < last) {
            $('#buttons').html("<button type='button' id='next' class='next' onClick='next()'>Next</a>");
        } else {
            $('#buttons').html("");
        }
        document.getElementById("activecell").textContent = 'solved';
        showfinished();
    }
};
// Back
function back() {
    var move = getmove();
    if (move.length > 0) {
        move.pop();
        savemove(move);
        drawboard();
    }
}
// Reset
function reset() {
    if (getmove().length > 0) {
        if (window.confirm(resetmessage())) {
            savemove([]);
            drawboard();
        }
    }
}
// Save note
function savenote() {
    var note = document.getElementById("note").value;
    localStorage.setItem("note", note);
}
// Next problem
function next() {
    var no = document.getElementById("no").value - 0;
    var last = document.getElementById("last").textContent - 0;
    if (no < last) {
        document.getElementById("no").value = no + 1;
        updatenum();
    }
}
// Scan duplicated numbers
function scancell(s, n) {
    var matched = 0;
    var match = new Array();
    var activecell = document.getElementById("activecell").textContent;
    var row = Math.floor(activecell / 9);
    var column = activecell % 9;
    var begin = Math.floor(row / 3) * 27 + Math.floor(column / 3) * 3;
    var box = [0, 1, 2, 9, 10, 11, 18, 19, 20];
    for (var i = 0; i < 9; i++) {
        if (s[begin + box[i]] == n && activecell != begin + box[i]) {
            match[matched] = begin + box[i];
            matched++;
        }
    }
    for (var i = 0; i < 9; i++) {
        if (s[row * 9 + i] == n && i != column) {
            match[matched] = row * 9 + i;
            matched++;
        }
        if (s[i * 9 + column] == n && i != row) {
            match[matched] = i * 9 + column;
            matched++;
        }
    }
    return match;
}
// Highlight the matching cells
function highlight(match) {
    var level = document.getElementById("level").value;
    var s = document.getElementById("current").textContent;
    for (var i = 0; i < match.length; i++) {
        document.getElementById(match[i]).innerHTML = "<div class='red'>" + s[match[i]] + "</div>";
    }
    var timeout_id = setTimeout(restorenumber, 5000);
}
// Finish highlight
function restorenumber() {
    var activecell = document.getElementById("activecell").textContent;
    var level = document.getElementById("level").value;
    var s = localStorage.getItem("s" + level);
    var c = document.getElementById("current").textContent;
    for (var i = 0; i < 81; i++) {
        if (c[i] != 0 && i != activecell) {
            if (s[i] == 0) {
                document.getElementById(i).innerHTML = button(i, c[i], 'cell');
            } else {
                document.getElementById(i).textContent = s[i];
            }
        }
    }
};
// Keyboard pressed
document.onkeydown = keydown;

function keydown(key) {
    // Check focus
    var focus = document.activeElement.id;
    if (focus == 'note' || focus == 'no') {
        return;
    }
    // get keycode and char
    var keycode = key.keyCode;
    var char = String.fromCharCode(keycode);
    // numeric key
    if (keycode > 48 && keycode < 58) {
        num(keycode - 48);
    }
    // backspace, delete key or x
    if (keycode == 8 || keycode == 46 || char == "X") {
        num(0);
    }
    // b: back
    if (char == "B") {
        back();
        return;
    }
    // r: restart
    if (char == "R") {
        reset();
        return;
    }
    // c: copyt to clipboard
    if (char == "C") {
        var current = document.getElementById("current").textContent;
        copyText(current);
        showcopied(current);
        return;
    }
    var activecell = document.getElementById("activecell").textContent;
    var level = document.getElementById("level").value;
    var s = localStorage.getItem("s" + level);
    if (activecell.length == 0) {
        return;
    }
    activecell = activecell - 0;
    // left arrow
    if (keycode == 37) {
        if (activecell % 9 > 0) {
            do {
                activecell -= 1;
            } while (s[activecell] != 0 && activecell % 9 > 0)
            if (s[activecell] == 0) {
                btn(activecell);
            }
        }
    }
    // up arrow
    if (keycode == 38) {
        if (activecell > 8) {
            do {
                activecell -= 9;
            } while (s[activecell] != 0 && activecell > 8)
            if (s[activecell] == 0) {
                btn(activecell);
            }
        }
    }
    // right arrow
    if (keycode == 39) {
        if (activecell % 9 < 8) {
            do {
                activecell += 1;
            } while (s[activecell] != 0 && activecell % 9 < 8)
            if (s[activecell] == 0) {
                btn(activecell);
            }
        }
    }
    // down arrow
    if (keycode == 40) {
        if (activecell < 72) {
            do {
                activecell += 9;
            } while (s[activecell] != 0 && activecell < 72)
            if (s[activecell] == 0) {
                btn(activecell);
            }
        }
    }
};
// Read sudoku data
function sudoku(data, level, no) {
    var lines = data.split("\n");
    var n = 0;
    var found = false;
    var line, s;
    for (var i = 0; i < lines.length; i++) {
        line = lines[i].split(" ");
        if (line[0] == level) {
            n++;
            if (!found) {
                s = line[1];
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
    if (screen.width > 640) {
        var ButtonRight = true;
        var board = "<table class='invisible'><tr class='invisible'><td class='invisible'>";
    } else {
        var ButtonRight = false;
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
                    var cell = x * 27 + i * 9 + y * 3 + j
                    if (s[cell] == 0) {
                        board += "<td class='internal' id='" + cell + "'>" + button(cell, ' ', 'cell') + "</td>";
                    } else {
                        board += "<td class='internal' id='" + cell + "'>" + s[cell] + "</td>";
                    }
                }
            }
            board += "</table></td>";
        }
    }
    board += "</table>";
    if (ButtonRight) {
        board += "<td class='invisible' style='width: 20px'>";
        board += "<td id='buttons' class='invisible'>";
        var w = 2;
    } else {
        board += "<p></p>";
        board += "<div id='buttons'>";
        var w = 5;
    }
    board += "<table class='invisible'>";
    for (i = 1; i < 10; i++) {
        if (i % w == 1) {
            board += "<tr>";
        }
        board += "<td class='invisible' id='n" + i + "'><button type='button' class='command' id='bn" + i +
            "' onClick='num(" + i + ")'>" + i + "</button>";
        if (i % w == 0) {
            board += "</tr>";
        }
    }
    board +=
        "<td class='invisible' id='del'><button type='button' class='command' id='del' onClick='num(0)'>X</button>";
    board +=
        "<tr><td class='invisible' id='back'><button type='button' class='command' id='back' onClick='back()'>B</button>";
    board +=
        "<td class='invisible' id='reset'><button type='button' class='command' id='reset' onClick='reset()'>R</button>";
    if (ButtonRight) {
        board += "<tr><td class='invisible'>" + getnote();
        var note = localStorage.getItem("note");
        if (note == null) {
            note = '';
        }
        board += "<tr><td class='invisible' colspan='2'><textarea id='note' rows='4' cols='12' onKeyup='savenote()'>" +
            note + "</textarea>";
    } else {
        board += "<div class='hidden' id='note'></div>";
    }
    board += "</tr></table>";
    if (ButtonRight) {
        board += "</table>";
    } else {
        board += "</div>";
    }
    return board;
}
// Deselect
function deselect(i) {
    document.getElementById(i).className = 'internal';
    var content = document.getElementById(i).innerHTML;
    content = content.replace(/<("[^"]*"|'[^']*'|[^'">])*>/g, '');
    if (content.length == 1) {
        var c = "cell";
    } else {
        if (content.length > 3) {
            var c = "mark";
        } else {
            var c = "mark3";
        }
    }
    $('#' + i).html("<button type='button' class='" + c + "' id='b" + i + "' onClick='btn(" + i + ")'>" + content +
        "</button>");
}
// Draw board
function drawboard() {
    var level = document.getElementById("level").value;
    var s = localStorage.getItem("s" + level);
    document.getElementById("current").textContent = s;
    var board = boardhtml(s);
    $('#board').html(board);
    var move = getmove();
    putmove(move);
    $('#message').text('');
    $('#activecell').text('');
}
// Copy text to clipboard
function copyText(text) {
    "use strict";
    var ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand("copy");
    ta.parentElement.removeChild(ta);
}
// Count numbers of blank cells
function numblank(s) {
    var blank = 0;
    for (var i = 0; i < 81; i++) {
        if (s[i] == 0) {
            blank++;
        }
    }
    return blank;
};
// Get move
function getmove() {
    var m = localStorage.getItem('move');
    if (m == null || m == '') return [];
    var move = m.split(' ');
    return move
}
// Save move
function savemove(move) {
    var m = move.join(' ');
    localStorage.setItem('move', m);
}
// Put moves
function putmove(move) {
    if (move.length > 0) {
        for (var i = 0; i < move.length; i++) {
            var n = move[i] % 10;
            var cell = (move[i] - n) / 10;
            btn(cell);
            num(n + 10);
            cell = document.getElementById("activecell").textContent;
            deselect(cell);
        }
    }
}
// Button
function button(cell, num, btnclass) {
   return "<button type='button' class='" + btnclass + "' id='b" + cell +
       "' onClick='btn(" + cell + ")'>" + num + "</button></td>";
}
// Show mesage
function showmessage(message) {
    document.getElementById("message").innerHTML = localmessage(message);
}
// get local message
function localmessage(message) {
    var lang = document.getElementById("lang").textContent;
    if (lang in message) {
        var message = message[lang];
    } else {
        var message = message['en'];
    }
    return message;
}
//////////////////////////////////
// Localization functions
// Level name
function getlevelname() {
    var lang = document.getElementById("lang").textContent;
    if (lang == 'ja') {
        var levelname = ['レベル', '簡単すぎ', '超簡単', '簡単', '普通', '難しい', 'とても難しい', '意地悪', '難しすぎ', '究極'];
    } else {
        var levelname = ['Level ', 'trivial', 'very easy', 'easy', 'normal', 'hard', 'very hard', 'evil', 'extreme',
            'ultimate'
        ];
    }
    return levelname;
}
// Problem No. translation
function getnoname() {
    return localmessage({
        en: 'No.',
        ja: '問題番号'
    })
}
// Note translation
function getnote() {
    return localmessage({
        en: 'note',
        ja: 'メモ'
    })
}
// Reset message
function resetmessage() {
    return localmessage({
        en: 'Restart the problem?',
        ja: '最初からやり直しますか?'
    })
}
// Show message when copied
function showcopied(current) {
    var en = "Current position<br>" + current + "<br>copied to clipboard."
    var ja = "現局面は<br>" + current + "<br>クリップボードにコピーしました。"
    showmessage({
        en: en,
        ja: ja
    });
}
// Show message when finished
function showfinished() {
    showmessage({
        en: 'This is the solution. Push Next button for next problem.',
        ja: 'これが正解です。Next ボタンで次の問題となります。'
    });
}
