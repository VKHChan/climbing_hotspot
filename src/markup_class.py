class MarkUp():
	def __init__(self):
		self.location_name = "name"
		self.location_long = "longitude"
		self.location_lat = "latitude"
		self.indoor_flag = "indoor"
		self.count = "count"

		self.groupby = [self.location_name, self.location_lat, self.location_long, self.indoor_flag]