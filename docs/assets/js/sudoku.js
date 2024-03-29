"use strict";
const startTime = Date.now();
const timeout = 60;
var modePencil = false;
var modeTime = false;
var rendering = false;
var loading = false;
var startGame = Date.now();
var timer = null;
var hints = 0;
var hint2 = "";
var hint3 = "";
var pyodide = "";
const special = ['800000000003600000070090200050007000000045700000100030001000068008500010090000400|Arto Inkala (2012)<br><br>As described in the <a href="https://www.sudokuwiki.org/Print_Arto_Inkala_Sudoku">article at sudoku.org</a>, this problem was described as the <strong>hardest sudoku</strong> in various news sites. Wait for several seconds to show hints.|Arto Inkala (2012)<br><br><a href="https://www.sudokuwiki.org/Print_Arto_Inkala_Sudoku">この記事</a>に書かれているように、<strong>最も難しい数独</strong>として色々なニュースサイトで紹介されました。ヒント表示には数秒待ってください。',
    '002800000030060007100000040600090000050600009000057060000300100070006008400000020|David Filmer (2012) The Weekly Extreme "Unsolveable" Sudoku Puzzle #49<br>See <a href="https://www.sudokuwiki.org/Print_Arto_Inkala_Sudoku">this article</a>.<br><br><strong>Warning</strong>: You may have to <strong>wait a minute</strong> for getting hint at the initial position. Browser will not respond in the period.|David Filmer (2012) The Weekly Extreme "Unsolveable" Sudoku Puzzle #49<br><a href="https://www.sudokuwiki.org/Print_Arto_Inkala_Sudoku">この記事</a>を参照。<br><br><strong>警告</strong>: 初期画面でHボタンを押すと<strong>思考時間が1分程度</strong>かかり、その間ブラウザが反応しなくなります。',
    '600008940900006100070040000200610000000000200089002000000060005000000030800001600|David Filmer (2011) The Weekly Extreme "Unsolveable" Sudoku Puzzle #28<br>See <a href="https://www.sudokuwiki.org/Print_Arto_Inkala_Sudoku">this article</a>.<br><br><strong>Warning</strong>: You may have to <strong>wait a few minutes</strong> for getting hint at the initial position. Browser will not respond in the period.|David Filmer (2011) The Weekly Extreme "Unsolveable" Sudoku Puzzle #28<br><a href="https://www.sudokuwiki.org/Print_Arto_Inkala_Sudoku">この記事</a>を参照。<br><br><strong>警告</strong>: 初期画面でHボタンを押すと<strong>思考時間が数分間</strong>かかり、その間ブラウザが反応しなくなります。'
]
$.ajax({
    url: 'https://raw.githubusercontent.com/sekika/kaidoku/master/kaidoku/data/sudoku.txt',
    success: function(data) {
        var pencil = localStorage.getItem("modePencil");
        if (pencil == null || pencil != 'on') {
            modePencil = false;
            localStorage.setItem("modePencil", 'off');
        } else {
            modePencil = true;
        }
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
            var move = getmove();
            if (no == 0 && move.length == 0) {
                s = null;
            }
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
        for (var i = 1; i <= 10; i++) {
            problem += "<option value='" + i + "'";
            if (i == level) {
                problem += " selected";
            }
            problem += ">"
            if (i < 10) {
                problem += levelname[0] + i + ": ";
            }
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
    error: function() {
        $('#board').html('Could not load sudoku problems.');
    }
});
async function loadpyodide() {
    if (pyodide != "" || loading) {
        return;
    }
    loading = true;
    console.log('Loading pyodide')
    pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");
    const micropip = await pyodide.pyimport("micropip");
    await micropip.install("kaidoku", false, false);
    console.log('Pyodide loaded')
    loading = false;
}
// Change the level
function updatelevel() {
    hints = 0;
    var data = document.getElementById("data").textContent;
    var level = document.getElementById("level").value;
    localStorage.setItem("level", level);
    var no = localStorage.getItem("level" + level);
    localStorage.setItem("note", '');
    modeTime = false;
    clearInterval(timer);
    if (no == null || no == 0) {
        if (no == null) {
            no = 1;
        }
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
    var no = parseInt(document.getElementById("no").value);
    localStorage.setItem("note", '');
    if (isFinite(no) && no > -1) {
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
    loadpyodide();
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
    if (!rendering && !modePencil && n != 0 && !content.includes(n)) {
        var match = scancell(s, n);
        if (match.length > 0) {
            highlight(match);
            showmessage({
                en: n.toString() + ' is a duplicate.',
                ja: n.toString() + 'は重複します。'
            });
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
            if (content.length > 5) {
                mark += ' ' + content.slice(5);
            }
        } else {
            var mark = '';
            for (let i = 1; i < 10; i++) {
                if (content.indexOf(i) > -1 || n + 0 == i) {
                    if (mark.length == 5) {
                        mark += ' ';
                    }
                    mark += i.toString();
                }
            }
        }
        if (mark.length > 1) {
            $('#' + activecell).html(button(activecell, mark, 'selectedmark'));
            s = s.slice(0, activecell - 81) + '0' + s.slice(activecell - 1 + 2);
            document.getElementById("current").textContent = s;
            return;
        }
        if (mark.length == 1) {
            n = mark;
            if (!rendering && !modePencil && n - 0 != 0) {
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
    if (!modeTime) {
        document.getElementById("message").innerHTML = "";
    }
    if (numblank(s) == 0) {
        // No blank cell
        // Check if finished
        var match = new Array();
        var box = [0, 1, 2, 9, 10, 11, 18, 19, 20];
        for (var i = 0; i < 9; i++) {
            var array = [];
            for (col = 0; col < 9; col++) {
                array.push(i * 9 + col);
            }
            if (duplicate(array) > 0) {
                notSolved('row ' + (i + 1).toString(), array);
                return;
            }
            var array = [];
            for (row = 0; row < 9; row++) {
                array.push(row * 9 + i);
            }
            if (duplicate(array) > 0) {
                notSolved('column ' + (i + 1).toString(), array);
                return;
            }
        }
        for (var row = 0; row < 3; row++) {
            for (var col = 0; col < 3; col++) {
                var numBox = row * 3 + col + 1;
                var begin = row * 27 + col * 3;
                var array = [];
                for (let b in box) {
                    array.push(begin + box[b]);
                }
                if (duplicate(array) > 0) {
                    notSolved('box ' + numBox.toString(), array);
                    return;
                }
            }
        }

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
        for (let i = 0; i < 81; i++) {
            if (document.getElementById(i).innerHTML.indexOf('button') > -1) {
                $('#' + i).html('<em><font color="blue">' + s[i] + '</font></em>');
            }
        }
        showfinished();
    }
};
// Check duplicate
function duplicate(arr) {
    let s = document.getElementById("current").textContent;
    let array = [];
    for (let i in arr) {
        array.push(s[arr[i]]);
    }
    for (let i = 1; i < 10; i++) {
        let num = i.toString();
        if (array.indexOf(num) != array.lastIndexOf(num)) {
            return i;
        }
    }
    return 0;
}
// Not solved
function notSolved(where, array) {
    let s = document.getElementById("current").textContent;
    let i = duplicate(array);
    if (!rendering) {
        let match = [];
        for (let j = 0; j < 9; j++) {
            if (s[array[j]] == i) {
                match.push(array[j]);
            }
        }
        highlight(match);
    }
    showmessage({
        en: 'Not solved. Duplicate ' + i.toString() + ' in ' + where + '.',
        ja: '解けていません。' + where + 'に' + i.toString() + 'が重複しています。'
    });
}
// Back
function back() {
    if (modePencil) {
        return;
    }
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
    if (modePencil) {
        return;
    }
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
    if (no > 0) {
        no = no + 1;
        if (no > last) {
            no = 1;
        }
    }
    document.getElementById("no").value = no;
    updatenum();
}
// Show hint
async function hint() {
    if (modePencil) {
        return;
    }
    if (hints > 0) {
        if (hints > 1) {
            document.getElementById("message").innerHTML = (hint2);
            if (hints > 2) {
                hint2 = hint3;
            }
        }
        return;
    }
    if (pyodide == "") {
        showwait();
        return;
    }
    await showthinking();
    let start = Date.now();
    let current = document.getElementById("current").textContent;
    let js_namespace = {
        pos: current
    };
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
        if (err.message.indexOf("ModuleNotFoundError") > -1) {
            showwait();
        } else {
            let mes = err.message.replace("\n", "<br>");
            showmessage({
                en: 'Pyodide error: ' + mes,
                ja: 'Pyodide エラー: ' + mes
            });
        }
        return
    }
    let time = Date.now() - start;
    let result = pyodide.globals.get("result");
    hint2 = pyodide.globals.get("hint2");
    hint3 = pyodide.globals.get("hint3");
    hints = parseInt(pyodide.globals.get("hints"));
    var lang = document.getElementById("lang").textContent;
    if (result.indexOf("Think candidates") > -1) {
        let strategy = ['Deep search', 'Search', 'Trial', 'Chain of pairs', 'Jellyfish', 'Swordfish', 'Hidden quad', 'Naked quad', 'Remote pairs', 'XYZ-wing', 'XY-wing', 'X-wing', 'Hidden triple', 'Hidden pair', 'Naked triple', 'Naked pair', 'Pointing triple', 'Pointing pair'];
        for (let s in strategy) {
            if (hint2.indexOf(strategy[s]) > -1) {
                if (lang == 'ja') {
                    result = '<a href="https://sekika.github.io/kaidoku/ja/logic">' + strategy[s] + '</a> を使います。';
                } else {
                    result = '<a href="https://sekika.github.io/kaidoku/logic">' + strategy[s] + '</a> is used.';
                }
                break;
            }
        }
    }
    if (result.indexOf("same value of") > -1) {
        let match = [];
        let i = -1;
        for (let j = 0; j < 2; j++) {
            i = result.indexOf("R", i + 1);
            match.push(parseInt(result[i + 1] - 1) * 9 + parseInt(result[i + 3]) - 1);
            console.log(match);
            highlight(match);
        }
    }
    if (result.indexOf("Look at Row") > -1) {
        let row = parseInt(result[result.indexOf("Row:") + 4]);
        let col = parseInt(result[result.indexOf("Column:") + 7]);
        btn((row - 1) * 9 + col - 1);
    }
    if (result.indexOf("Hidden single") > -1) {
        let array = [];
        if (result.indexOf("row") > -1) {
            let row = parseInt(result[result.indexOf("row") + 4]) - 1;
            for (let i = 0; i < 9; i++) {
                array.push(row * 9 + i);
            }
        }
        if (result.indexOf("column") > -1) {
            let col = parseInt(result[result.indexOf("column ") + 7]) - 1;
            for (let i = 0; i < 9; i++) {
                array.push(i * 9 + col);
            }
        }
        if (result.indexOf("box") > -1) {
            let box = parseInt(result[result.indexOf("box") + 4]) - 1;
            let b = (Math.floor(box / 3)) * 27 + (box % 3) * 3;
            array = [b, b + 1, b + 2, b + 9, b + 10, b + 11, b + 18, b + 19, b + 20];
        }
        let blank = [];
        for (let i in array) {
            if (current[array[i]] == 0) {
                blank.push(array[i]);
            }
        }
        for (let i in blank) {
            document.getElementById(blank[i]).style.backgroundColor = 'lightgreen';
        }
        let timeout_id = setTimeout(restoreblank, 150);
    }
    if (lang == 'ja') {
        if (result.indexOf("same value of") > -1) {
            result = result.replace("Both ", "");
            result = result.replace("and", "と");
            result = result.replace("have the same value of", "で");
            result = result.replace(".", " が重複しています。");
        }
        if (result == 'No solution to this position. There should be a mistake up to here. You can take back a move with B.') {
            result = 'この状態では解はありません。どこかで間違えました。Bで戻れます。';
        }
        if (result.indexOf("Look at Row") > -1) {
            result = result.replace("Look at Row:", "上から");
            result = result.replace(" Column:", "行目、左から");
            result = result.replace(". What number is available?", "列目には何が入りますか？");
        }
        if (result.indexOf("Hidden single") > -1) {
            result = result.replace("Hidden single in ", "");
            result = result.replace("row", "（上から数えて）row");
            result = result.replace("column", "（左から数えて）column");
            result = result.replace("box", "（左上から右に数えて）box");
            result = result.replace("can be found.", "に単独候補マスがあるよ。");
        }
        if (hint2.indexOf("Hidden single") > -1) {
            hint2 = hint2.replace("Hidden single in ", "");
            hint2 = hint2.replace("for", "に単独候補マスの") + " があるよ。";
        }
        if (result.indexOf("Think candidates") > -1) {
            result = result.replace("Think candidates of the cells.", "数字の候補を考えよう。");
        }
        if (hint2.indexOf("successively") > -1) {
            hint2 = hint2.replace("Use", '次の<a href="https://sekika.github.io/kaidoku/ja/logic">解法</a>を順番に使うと1マス確定するよ。<br>');
            hint2 = hint2.replace("successively.", "");
        }
    }
    if (hint2.indexOf("Use") == 0) {
        hint2 = hint2.replace("Use", '<a href="https://sekika.github.io/kaidoku/logic">Use</a>');
    }
    var add = "<br>Push H for additional hint.";
    if (lang == 'ja') {
        add = "<br>Hでさらにヒントを表示します。";
    }
    if (hints > 1) {
        result += add;
    }
    if (hints > 2) {
        hint2 += add;
        hint3 = hint3.replace(/\n/g, "<br>");
    }
    if (time > 1000) {
        let sec = (Math.floor(time / 100) / 10).toString();
        result += {
            en: '<br>(Thinking time: ' + sec + ' seconds)',
            ja: '<br>(思考時間 ' + sec + '秒)'
        } [document.getElementById("lang").textContent];
    }
    document.getElementById("message").innerHTML = result;
}

// Restore blank cell
function restoreblank() {
    var c = document.getElementById("current").textContent;
    for (var i = 0; i < 81; i++) {
        if (c[i] == 0) {
            document.getElementById(i).style.backgroundColor = '';
        }
    }
};

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
        // if (c[i] != 0 && i != activecell) {
        if (c[i] != 0) {
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
    // p: pencil mode
    if (char == "P") {
        pencil();
        return;
    }
    // c: copyt to clipboard
    if (char == "C") {
        if (modePencil) {
            return;
        }
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
    modeTime = false;
    clearInterval(timer);
    if (level == 10) {
        let last = special.length;
        if (no == 0) {
            no = 1;
        }
        if (no > last) {
            no = last;
        }
        s = special[no - 1].split("|")[0];
        return [s, last];
    }
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
    if (no == 0) {
        no = Math.floor(Math.random() * n) + 1;
        [s, n] = sudoku(data, level, no);
        s = shuffle(s);
        if (modePencil) {
            startTimer();
        }
    }
    return [s, n];
}
// Start timer
function startTimer() {
    modeTime = true;
    startGame = Date.now();
    timer = setInterval("showTime()", 1000)
}
// Shuffle number and rotation
function shuffle(s) {
    let rot = Math.floor(Math.random() * 8);
    // Fisher–Yates shuffle
    let shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    for (let i = 8; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [shuffle[i], shuffle[j]] = [shuffle[j], shuffle[i]];
    }
    let flipRow = ((rot & 4) == 4);
    let flipCol = ((rot & 2) == 2);
    let flipRC = ((rot & 1) == 1);
    let flip = '';
    for (let i = 0; i < 81; i++) {
        let row = Math.floor(i / 9);
        let col = i % 9;
        if (flipRow) {
            row = 8 - row;
        }
        if (flipCol) {
            col = 8 - col;
        }
        if (flipRC) {
            [row, col] = [col, row];
        }
        let cell = parseInt(s[row * 9 + col]);
        if (cell > 0) {
            cell = shuffle[cell - 1];
        }
        flip += cell.toString();
    }
    return flip;
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
        "<tr><td class='invisible' id='pencil'><button type='button' class='command' id='pencil' onClick='pencil()'>P</button>";
    board +=
        "<td class='invisible' id='back'><button type='button' class='command' id='back' onClick='back()'>B</button>";
    if (ButtonRight) {
        board += "<tr>";
    }
    board +=
        "<td class='invisible' id='reset'><button type='button' class='command' id='reset' onClick='reset()'>R</button>";
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
    rendering = true;
    var level = document.getElementById("level").value;
    var s = localStorage.getItem("s" + level);
    document.getElementById("current").textContent = s;
    var board = boardhtml(s);
    $('#board').html(board);
    var move = getmove();
    if (move.length == 0) {
        showstart();
    } else {
        $('#message').text('');
        putmove(move);
    }
    $('#activecell').text('');
    if (modePencil) {
        hideButtons();
    }
    rendering = false;
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
// Pencil mode
function pencil() {
    if (modePencil) {
        pencilOff();
    } else {
        pencilOn();
    }
}
// Pencil mode off
function pencilOff() {
    modePencil = false;
    modeTime = false;
    clearInterval(timer);
    localStorage.setItem('modePencil', 'off');
    showPencilOff();
    document.getElementById('back').style.visibility = 'visible';
    document.getElementById('reset').style.visibility = 'visible';
    document.getElementById('hint').style.visibility = 'visible';
}
// Pencil mode on
function pencilOn() {
    modePencil = true;
    localStorage.setItem('modePencil', 'on');
    showPencilOn();
    hideButtons();
}
// Hide bottuns
function hideButtons() {
    document.getElementById('back').style.visibility = 'hidden';
    document.getElementById('reset').style.visibility = 'hidden';
    document.getElementById('hint').style.visibility = 'hidden';
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
        var levelname = ['レベル', '簡単すぎ', '超簡単', '簡単', '普通', '難しい', 'とても難しい', '意地悪', '難しすぎ', '究極', '特別問題'];
    } else {
        var levelname = ['Level ', 'trivial', 'very easy', 'easy', 'normal', 'hard', 'very hard', 'evil', 'extreme',
            'ultimate', 'Special problem'
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
// Show message when starting
function showstart() {
    let level = document.getElementById("level").value;
    let no = document.getElementById("no").value - 0;
    if (level == 10) {
        let lang = {
            en: 1,
            ja: 2
        } [document.getElementById("lang").textContent];
        if (no == 0) {
            no = 1;
        }
        let description = special[no - 1].split("|")[lang];
        showmessage({
            en: 'Special problem No. ' + no.toString() + '<br>' + description,
            ja: '特別問題 No. ' + no.toString() + '<br>' + description
        });
        return;
    }
    if (no == 0) {
        showrandom();
        return;
    }
    showmessage({
        en: 'Starting a new game. You can select another problem from the level and number.',
        ja: 'ゲームを開始します。レベルと番号から他の問題を選ぶことができます。'
    });
}
// Starting a random problem
function showrandom() {
    let level = document.getElementById("level").value;
    if (modeTime) {
        showmessage({
            en: 'Starting a time trial mode in level ' + level + '. When you turn off the pencil mode, time trial is finished.',
            ja: 'レベル' + level + 'のタイムトライアルを開始します。鉛筆モードをオフにすると、タイムトライアルが終わります。'
        });
        return;
    }
    showmessage({
        en: 'Starting a random game in level ' + level + '.',
        ja: 'レベル' + level + 'のランダムな問題を開始します。'
    });
}
// Show message when finished
function showfinished() {
    if (modeTime) {
        clearInterval(timer);
        let level = document.getElementById("level").value;
        let time = parseInt((Date.now() - startGame) / 1000);
        showmessage({
            en: 'Level ' + level + ' solved in ' + enTime(time) + '.',
            ja: 'レベル' + level + 'を' + jpTime(time) + 'で解きました。'
        });
    } else {
        showmessage({
            en: 'This is the solution. Push Next button for next problem.',
            ja: 'これが正解です。Next ボタンで次の問題となります。'
        });
    }
}
// Show time
function showTime() {
    let time = parseInt((Date.now() - startGame) / 1000);
    if (time < 10) {
        return;
    }
    showmessage({
        en: 'Time trial: ' + enTime(time),
        ja: 'タイムトライアル: ' + jpTime(time)
    });
}

function enTime(time) {
    let min = Math.floor(time / 60);
    let sec = time % 60;
    if (min == 0) {
        return sec.toString() + '′';
    }
    return min.toString() + '°' + sec.toString() + "′";
}

function jpTime(time) {
    let min = Math.floor(time / 60);
    let sec = time % 60;
    let s = '';
    if (min > 0) {
        s = min.toString() + '分';
    }
    return s + sec.toString() + "秒";
}
// Show message for pencil mode on
function showPencilOn() {
    showmessage({
        en: 'Now we are in pencil mode. In pencil mode, checking duplicate of numbers and giving hints are disabled. It is same as solving with a pencil. Pencil mode can be turned off by pushing P button again.',
        ja: '鉛筆モードに入ります。鉛筆モードでは、数字の重複自動チェックやヒント機能などは使えません。紙と鉛筆で解く状態と同じとなります。再度Pボタンを押すと通常モードに戻ります。'
    });
}
// Show message for pencil mode off
function showPencilOff() {
    showmessage({
        en: 'Pencil mode is turned off.',
        ja: '鉛筆モードをオフにします。'
    });
}
// Show message when pyodide is not loaded yet
function showwait() {
    if (Date.now() - startTime < timeout * 1000) {
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
// Show thinking
function showthinking() {
    showmessage({
        en: 'Thinking...',
        ja: '思考中...'
    });
    // Wait 0.01 seconds for drawing if level>7 and blankcell>45
    let level = document.getElementById("level").value;
    let s = document.getElementById("current").textContent;
    if (level > 7 && numblank(s) > 45) {
        let milliseconds = 10;
        return new Promise(resolve => {
            setTimeout(resolve, milliseconds);
        });
    }
}