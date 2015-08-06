require('./module_a');//绝对模块和相对模块
require('./module_b');//原因在于这两个模块并没有通过NPM来安装，也不在node_modules目录中，而且Node自带模块中没有以此为名的模块