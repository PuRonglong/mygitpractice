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
		<?php
		class Person{
			function _construnct($name,$sex){
				$this->name=$name;
				$this->sex=$sex;
			}

			function showName(){
				echo $this->name;
			}

			function showSex(){
				echo $this->sex;
			}
		}
		class Worker extends Person{
			function _construct($name,$sex,$job){
				parent::__construct($name,$sex);

				$this->job=$job;
			}
			function showJob(){
				echo $this->job;
			}
		}

		$w1=new Worker('blue','男','打杂的');

		$w1->showSex();
		?>
	</body>
</html>