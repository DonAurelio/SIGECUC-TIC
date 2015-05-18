class SingletonUser:

	def __init__(self,request):
		self.singleton_user = None
		self.id = request.user.id

	@staticmethod
	def get_instance(self,request):
		if self.singleton_user == None:
			self.singleton_user = SingletonUser(request)
			return self.singleton_user
		else:
			return self.singleton_user

