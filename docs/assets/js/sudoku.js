"use strict";
const startTime = Date.now();
const timeout = 60;
var hints = 0;
var hint2 = "";
var hint3 = "";
var pyodide = "";
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
        loadpyodide();
    },
    error: function () {
        $('#board').html('Could not load sudoku problems.');
    }
});
async function loadpyodide() {
    pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");
    const micropip = await pyodide.pyimport("micropip");
    await micropip.install("kaidoku", false, false);
}
// Change the level
function updatelevel() {
    hints = 0;
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
    hints = 0;
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
    hints = 0;
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
    hints = 0;
    var move = getmove();
    if (move.length > 0) {
        move.pop();
        savemove(move);
        drawboard();
    }
}
// Reset
function reset() {
    hints = 0;
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
    hints = 0;
    var no = document.getElementById("no").value - 0;
    var last = document.getElementById("last").textContent - 0;
    if (no < last) {
        document.getElementById("no").value = no + 1;
        updatenum();
    }
}
// Show hint
async function hint() {
    if ( hints > 0 ) {
        if ( hints > 1 ) {
            document.getElementById("message").innerHTML = (hint2);
            if ( hints > 2 ) {
                hint2 = hint3;
            }
        }
        return;
    }
    if ( pyodide == "" ) {
        showwait();
        return;
    }
    let current = document.getElementById("current").textContent;
    let js_namespace = { pos : current };
    pyodide.registerJsModule("js_namespace", js_namespace);
    try {
        pyodide.runPython(`
            from js_namespace import pos
            import kaidoku
            import sys
            k = kaidoku.Kaidoku(pos)
            del sys.modules["js_namespace"]
            if not k.valid:
                result = k.mes
            else:
                result = k.hint
            hints = k.hints
            if hints == 0:
                hints = 1
            hint2 = hint3 = ''
            if hints > 1:
                hint2 = k.hint2
            if hints > 2:
                hint3 = k.hint3
        `);
    } catch (err) {
        // showmessage(err);
        if ( err.message.indexOf("ModuleNotFoundError") > -1 ) {
            showwait();
        } else {
            let mes = err.message.replace("\n","<br>");
            showmessage({
                en: 'Pyodide error: ' + mes,
                ja: 'Pyodide エラー: ' + mes
            });
        }
        return
    }
    // pyodide.unregisterJsModule("js_namespace");
    // js_namespace = '';
    let result = pyodide.globals.get("result");
    hint2 = pyodide.globals.get("hint2");
    hint3 = pyodide.globals.get("hint3");
    hints = parseInt(pyodide.globals.get("hints"));
    var lang = document.getElementById("lang").textContent;
    if ( lang == 'ja' ) {
        if ( result == 'No solution to this position' ) {
            result = 'この状態では解はありません。どこかで間違えました。Bで戻れます。';
        }
        if ( result.indexOf("Look at Row") > -1 ) {
            result = result.replace("Look at Row:", "上から");
            result = result.replace(" Column:", "行目、左から");
            result = result.replace(". What number is available?", "列目には何が入りますか？");
        }
        if ( result.indexOf("Hidden single") > -1 ) {
            result = result.replace("Hidden single in ", "");
            result = result.replace("row", "（上から数えて）row");
            result = result.replace("column", "（左から数えて）column");
            result = result.replace("box", "（左上から右に数えて）box");
            result = result.replace("can be found.", "に単独候補マスがあるよ。");
        }
        if ( hint2.indexOf("Hidden single") > -1 ) {
            hint2 = hint2.replace("Hidden single in ", "");
            hint2 = hint2.replace("for", "に単独候補マスの") + " があるよ。";
        }
        if ( result.indexOf("Think candidates") > -1 ) {
            result = result.replace("Think candidates of the cells.", "数字の候補を考えよう。");
        }
        if ( hint2.indexOf("successively") > -1 ) {
            hint2 = hint2.replace("Use", '次の<a href="https://sekika.github.io/kaidoku/ja/logic">解法</a>を順番に使うと1マス確定するよ。<br>');
            hint2 = hint2.replace("successively.", "");
        }
    }
    if ( hint2.indexOf("Use") == 0 ) {
        hint2 = hint2.replace("Use", '<a href="https://sekika.github.io/kaidoku/logic">Use</a>');
    }
var add = "<br>Push H for additional hint.";
    if ( lang == 'ja' ) {
        add = "<br>Hでさらにヒントを表示します。";
    }
    if ( hints > 1 ) {
        result += add;
    }
    if ( hints > 2 ) {
        hint2 += add;
        hint3 = hint3.replace("\n", "<br>");
    }
    document.getElementById("message").innerHTML = (result);
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
    // h: show hint
    if (char == "H") {
        hint();
        return;
    }
    hints = 0;
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
        board += "<tr>";
    }
    board +=
        "<td class='invisible' id='hint'><button type='button' class='command' id='hint' onClick='hint()'>H</button>";
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
// Show message when pyodide is not loaded yet
function showwait() {
    if ( Date.now() - startTime < timeout * 1000 ) {
        showmessage({
            en: 'Not ready to show hint yet. Wait for a moment and press H again.',
            ja: 'まだヒント表示の準備ができていません。少し待ってからもう一度 H ボタンを押してください。'
        });
    } else {
        showmessage({
            en: 'Could not load <a href="https://pyodide.org/en/stable/">pyodide</a> for showing hint. You can try different web browser. See <a href="https://pyodide.org/en/stable/usage/index.html">supported browsers</a>.',
            ja: 'ヒント表示に必要な <a href="https://pyodide.org/en/stable/">pyodide</a> を読み込めませんでした。他のWebブラウザを試してみてください。<a href="https://pyodide.org/en/stable/usage/index.html">Pyodide がサポートするブラウザ</a>を参考にしてください。'
        });
    }
}
