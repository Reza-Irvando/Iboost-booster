from app import app
from app.controllers import segment

app.route ("/content/segment/list", methods = ["GET"])(segment.SegmentList)
app.route ("/content/segment/create", methods = ["POST"])(segment.SegmentCreate)
app.route ("/content/segment/detail", methods = ["GET"])(segment.SegmentDetail)
app.route ("/content/segment/update", methods = ["PUT"])(segment.SegmentUpdate)
app.route ("/content/segment/delete", methods = ["DELETE"])(segment.SegmentDelete)