% if items:
	<p>These are the open items:</p>
	<ul>
	% for item in items:
		<li>{{item["task"]}}</li>
	%end
	</ul>
% else:
	<p>There are no open items</p>
%end
