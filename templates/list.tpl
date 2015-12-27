<a href="/todo/new">Create a new item</a>

% if items:
	<p>These are the open items:</p>
	<ul>
	% for item in items:
		<li>{{item["task"]}}</a>&nbsp;<a href="/todo/{{item["_id"]}}/edit">Edit</a>&nbsp;<a href="/todo/{{item["_id"]}}/delete">Delete</a></li>
	%end
	</ul>
% else:
	<p>There are no open items</p>
%end
