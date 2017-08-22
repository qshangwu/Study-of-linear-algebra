import math

class Vector(object):
	"""docstring for Vector"""
	def __init__(self, coodinates):
		self.coodinates = tuple(coodinates)
		self.dimension = len(coodinates)
	def __str__(self):
		return "Vector is: {}".format(self.coodinates)
	def __eq__(self,v):
		return self.coodinates == v.coodinates

def Plus(v1,v2):
	v_sum = []
	for i in range(v1.dimension):
		v_s =float(v1.coodinates[i]) + float(v2.coodinates[i])
		v_sum.append(v_s)
	return Vector(v_sum)

def Mius(v1,v2):
	v_minus = []
	for i in range(v1.dimension):
		v_m = v1.coodinates[i] - v2.coodinates[i]
		v_minus.append(v_m)
	return Vector(v_minus)

def  Scale(v1,m = 1):
	v_scale = []
	for i in range(v1.dimension):
		v_s = v1.coodinates[i] * m
		round(v_s,3)
		v_scale.append(v_s)
	return Vector(v_scale)
def Mag(v):
	v_mag = float(0)
	for i in range(v.dimension):
		v_mag = v_mag +v.coodinates[i]**2
	return v_mag**(0.5)

def Normal(v):
	mag_v = Mag(v)
	return Vector([i/mag_v for i in v.coodinates])
	
def Dot_Product(v1,v2):
	v_DP = [x * y for x,y in zip(v1.coodinates,v2.coodinates)]
	return sum(v_DP)

def Angle(v1,v2):
	return math.acos(Dot_Product(Normal(v1),Normal(v2)))

def Position_Check(v1,v2):
	Position_Info = Dot_Product(v1,v2)
	if Position_Info == 0:
	 	print "Vectors are Orthogonality!"

def Projection(v, v_base):
	i_base = Normal(v_base)
	return Scale(i_base,Dot_Product(v,i_base))

def Orthogonal(v,v_base):
	v_projection = Projection(v,v_base)
	return Mius(v,v_projection)