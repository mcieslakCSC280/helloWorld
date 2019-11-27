class delivery_personnel:
	def __init__ (self, name = None, years_of_service, company, is_drone, zip_codes_covered):
		self.years_of_service = years_of_service
		self.company = company
		self.is_drone = is_drone
		self.zip_codes_covered = zip_codes_covered

	def get_yos(self)
		return(self.years_of_service)

	def set_yos(self, d)
		self.years_of_service = d

	def get_company(self)
		return(self.company)

	def set_company(self, d)
		self.company = d

	def get_zip_covered(self)
		return(self.zip_codes_covered)

	def set_zip_covered(self, d)
		self.zip_codes_covered = d

	def deliver(self, d)
	dlist = list(d)
	if(len(dlist) == 0):
		return(False)
	else:
		for i in dlist:
			if(dlist[i] in self.get_zip_covered()):
				dlist.remove(dlist[i])
				deliver(dlist)
			

def main():
	zipList = [20016, 20017, 20018, 20019, 20020]
	deliver(zipList)
	


if __name__ == "__main__":
	main()

		