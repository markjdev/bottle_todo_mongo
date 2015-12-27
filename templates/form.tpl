<form method="POST">
	<label for="task">Task:</label><input type="text" id="task" name="task" value="{{task}}" />

	%if error:
	<p>* Task must be specified</p>
	%end
	
	<input type="submit" name="Save" />
</form>
