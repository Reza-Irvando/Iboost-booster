from app import app
from app.controllers import blastStatus

app.route ("/master/blastStatus/list", methods = ["GET"])(blastStatus.BlastStatusList)
app.route ("/master/blastStatus/create", methods = ["POST"])(blastStatus.BlastStatusCreate)
app.route ("/master/blastStatus/detail", methods = ["GET"])(blastStatus.BlastStatusDetail)
app.route ("/master/blastStatus/update", methods = ["PUT"])(blastStatus.BlastStatusUpdate)
app.route ("/master/blastStatus/delete", methods = ["DELETE"])(blastStatus.BlastStatusDelete)