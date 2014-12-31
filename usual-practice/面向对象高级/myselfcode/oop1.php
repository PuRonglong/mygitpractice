<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>未命名</title>
		<link rel="stylesheet" type="text/css" href="" />
		<style type="text/css">
			
		</style>
		<script type="text/javascript" src=""></script>
		<script type="text/javascript">
			
		</script>
	</head>
	<body>
		<?php//php服务端标记
		/*$a=12;
		$b=5;
		echo $a+$b;*/
/*
		$a='abc';
		$b='123';

		echo $a.$b;*/

		class Person{
			function _construnct($name,$sex){
				$this->name=$name;
				$this->sex=$sex;
			}

			function showName(){
				echo $this->name;
			}

			function sex(){
				echo $this->sex;
			}
		}
		$p1=new Person('蒲荣龙','男');

		$p1->showName();
		?>
	</body>
</html>