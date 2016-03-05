function createArray() {

    var arr = new Array();

    for (var i = 0; i < 10; i++) {

        arr[i] = function () {

        return i;

        };

    }

    return arr;

    }

    var funcs = createArray();

    for (var i = 0; i < funcs.length; i++) {

    document.write(funcs[i]() + "<br />");

    }