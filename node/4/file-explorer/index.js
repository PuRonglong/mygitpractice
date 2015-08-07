var fs = require('fs')
    , stdin = process.stdin
    ,stdout = process.stdout;

//fs.readdir(__dirname,function(err,files){
//    console.log(files);
//})//为了获取文件列表，我们需要使用fs.readdir

//called for each file walked in the directory
function file(i) {
    var filename = files[i];

    fs.stat(__dirname + '/' + filename, function (err, stat) {
        if (stat.isDirectoty()) {
            console.log('   ' + i + '\033[36' + filename + '/\033[39m');
        } else {
            console.log('   ' + i + '033[90m' + filename + '\033[39m');
        }//回调函数中，同时还给出了错误对象(如果有的话)和一个stat对象。
        // 本例中所使用的stat对象上的方法是isDirectory，如果路径所代表的是目录，我们就用有别于文件的颜色标识出来
        if (++i == files.length) {
            read();//如果所有文件都处理完毕，此时提示用户进行选择
        } else {
            file(i);
        }
    });
}

//read user input when files are shown
function read(){
    console.log('');//为了输出更友好，我们先输出一段空行
    stdout.write('  \033[33mEnter your choice:  \033[39m');//使用rocess.stdout.write而不是console.log；
    // 这样就无须换行，让用户可以直接在提示语后进行输入
    stdin.resume();//用户等待用户输入
    stdin.setEncoding('utf-8');//设置流编码为utf-8,这样就能支持特殊字符了

    stdin.on('data',option);//读取用户输入后，接下来要做的就是根据欧诺个户输入做出相应处理。所以开始监听其data事件
}