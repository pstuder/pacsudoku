import unittest
from solver import Algorithm, Norvig
from validmatrix import MatrixHandler

class TestAlgorithm(unittest.TestCase):
	def setUp(self):
		
		# Values to test cross(A, B)
		#---------------------------------------------------------------------
		self.A = 'ABC'
		self.B = '123'
		self.crossAB = ['A1', 'A2', 'A3',\
						'B1', 'B2', 'B3',\
						'C1', 'C2', 'C3']
		#---------------------------------------------------------------------
		
		# Values to test some(sequence)
		#---------------------------------------------------------------------
		self.sequence = self.A + self.B
		self.sequence_negative = [''*20]
		self.expected_element = self.A[0]
		#---------------------------------------------------------------------
	def test_cross(self):
		algorithm = Algorithm(MatrixHandler([]))
		self.assertEqual(self.crossAB,algorithm._cross(self.A,self.B))

	def test_some(self):
		algorithm = Algorithm(MatrixHandler([]))
		self.assertEqual(self.expected_element,\
										algorithm._some(self.sequence))
	
	def test_some_negative(self):
		algorithm = Algorithm(MatrixHandler([]))
		self.assertFalse(algorithm._some(self.sequence_negative))

class TestNorvigAlgorithm(unittest.TestCase):
	def setUp(self):
	
		# Values to test converting to grid
		#---------------------------------------------------------------------
		self.matrix = [ [4, 0, 0, 0, 0, 0, 8, 0, 5],\
						[0, 3, 0, 0, 0, 0, 0, 0, 0],\
						[0, 0, 0, 7, 0, 0, 0, 0, 0],\
						[0, 2, 0, 0, 0, 0, 0, 6, 0],\
						[0, 0, 0, 0, 8, 0, 4, 0, 0],\
						[0, 0, 0, 0, 1, 0, 0, 0, 0],\
						[0, 0, 0, 6, 0, 3, 0, 7, 0],\
						[5, 0, 0, 2, 0, 0, 0, 0, 0],\
						[1, 0, 4, 0, 0, 0, 0, 0, 0] ]
		self.mtrxhandler = MatrixHandler(self.matrix)
		
		self.grid = {'A1':'4', 'A2':'0', 'A3':'0', 'A4':'0', 'A5':'0',\
					 'A6':'0', 'A7':'8', 'A8':'0', 'A9':'5',\
					 'B1':'0', 'B2':'3', 'B3':'0', 'B4':'0', 'B5':'0',\
					 'B6':'0', 'B7':'0', 'B8':'0', 'B9':'0',\
					 'C1':'0', 'C2':'0', 'C3':'0', 'C4':'7', 'C5':'0',\
					 'C6':'0', 'C7':'0', 'C8':'0', 'C9':'0',\
					 'D1':'0', 'D2':'2', 'D3':'0', 'D4':'0', 'D5':'0',\
					 'D6':'0', 'D7':'0', 'D8':'6', 'D9':'0',\
					 'E1':'0', 'E2':'0', 'E3':'0', 'E4':'0', 'E5':'8',\
					 'E6':'0', 'E7':'4', 'E8':'0', 'E9':'0',\
					 'F1':'0', 'F2':'0', 'F3':'0', 'F4':'0', 'F5':'1',\
					 'F6':'0', 'F7':'0', 'F8':'0', 'F9':'0',\
					 'G1':'0', 'G2':'0', 'G3':'0', 'G4':'6', 'G5':'0',\
					 'G6':'3', 'G7':'0', 'G8':'7', 'G9':'0',\
					 'H1':'5', 'H2':'0', 'H3':'0', 'H4':'2', 'H5':'0',\
					 'H6':'0', 'H7':'0', 'H8':'0', 'H9':'0',\
					 'I1':'1', 'I2':'0', 'I3':'4', 'I4':'0', 'I5':'0',
					 'I6':'0', 'I7':'0', 'I8':'0', 'I9':'0'}
		#---------------------------------------------------------------------
		
		# Values to test construct_possible_values_grid
		#---------------------------------------------------------------------
		self.grid_possible_values = {'A1':'4', 'A2':'1679', 'A3':'12679',\
									 'A4':'139', 'A5':'2369', 'A6':'269',\
									 'A7':'8','A8':'1239', 'A9':'5',\
									 #-----------------------------------------
									 'B1':'26789', 'B2':'3', 'B3':'1256789',\
									 'B4':'14589', 'B5':'24569',\
									 'B6':'245689', 'B7':'12679',\
									 'B8':'1249', 'B9':'124679',\
									 #-----------------------------------------
									 'C1':'2689', 'C2':'15689', 'C3':'125689',\
									 'C4':'7', 'C5':'234569', 'C6':'245689',\
									 'C7':'12369', 'C8':'12349',\
									 'C9':'123469',\
									 #-----------------------------------------
									 'D1':'3789', 'D2':'2', 'D3':'15789',\
									 'D4':'3459', 'D5':'34579', 'D6':'4579',\
									 'D7':'13579', 'D8':'6', 'D9':'13789',\
									 #-----------------------------------------
									 'E1':'3679', 'E2':'15679', 'E3':'15679',\
									 'E4':'359', 'E5':'8', 'E6':'25679',\
									 'E7':'4', 'E8':'12359', 'E9':'12379',\
									 #-----------------------------------------
									 'F1':'36789','F2':'4', 'F3':'56789',\
									 'F4':'359', 'F5':'1', 'F6':'25679',\
									 'F7':'23579', 'F8':'23589', 'F9':'23789',\
									 #-----------------------------------------
									 'G1':'289','G2':'89','G3':'289','G4':'6',\
									 'G5':'459','G6':'3','G7':'1259','G8':'7',\
									 'G9':'12489',\
									 #-----------------------------------------
									 'H1':'5', 'H2':'6789', 'H3':'3',\
									 'H4':'2', 'H5':'479', 'H6':'1',\
									 'H7':'69', 'H8':'489', 'H9':'4689',\
									 #-----------------------------------------
									 'I1':'1', 'I2':'6789', 'I3':'4',\
									 'I4':'589', 'I5':'579', 'I6':'5789',\
									 'I7':'23569', 'I8':'23589', 'I9':'23689'}
		#---------------------------------------------------------------------
		
		# Values to test assign and eliminate
		#---------------------------------------------------------------------
		self.field = 'F4'
		self.value_valid = '9'
		self.value_with_contradiction = '6'
		self.grid_contradiction = {'F4':'6'}
		#---------------------------------------------------------------------
		
		# Values to test search and solve
		#---------------------------------------------------------------------
		self.matrix_multiple = [[0, 8, 0, 0, 0, 9, 7, 4, 3],\
								[0, 5, 0, 0, 0, 8, 0, 1, 0],\
								[0, 1, 0, 0, 0, 0, 0, 0, 0],\
								[8, 0, 0, 0, 0, 5, 0, 6, 0],\
								[0, 0, 0, 8, 0, 4, 0, 0, 0],\
								[0, 0, 0, 3, 0, 0, 0, 0, 6],\
								[0, 0, 0, 0, 0, 0, 0, 7, 0],\
								[0, 3, 0, 5, 0, 0, 0, 8, 0],\
								[9, 7, 2, 4, 0, 0, 0, 5, 0]]
		self.mtrxhandler_multiple = MatrixHandler(self.matrix_multiple)
		
		self.matrix_unsolvable = [ [1, 2, 3, 4, 5, 6, 7, 8, 0],\
									[0, 0, 0, 0, 0, 0, 0, 0, 2],\
									[0, 9, 0, 1, 0, 0, 0, 0, 3],\
									[0, 0, 0, 0, 0, 0, 0, 0, 4],\
									[0, 0, 0, 0, 7, 0, 0, 0, 5],\
									[0, 0, 0, 0, 0, 0, 0, 0, 6],\
									[0, 0, 0, 0, 1, 0, 0, 0, 7],\
									[0, 0, 1, 0, 0, 2, 0, 0, 8],\
									[0, 0, 0, 0, 0, 0, 0, 0, 9] ]
		self.mtrxhandler_unsolvable = MatrixHandler(self.matrix_unsolvable)
		
		self.grid_solved = {'A1':'4', 'A2':'1', 'A3':'7', 'A4':'3', 'A5':'6',\
							'A6':'9', 'A7':'8', 'A8':'2', 'A9':'5',\
							'B1':'6', 'B2':'3', 'B3':'2', 'B4':'1', 'B5':'5',\
							'B6':'8', 'B7':'9', 'B8':'4', 'B9':'7',\
							'C1':'9', 'C2':'5', 'C3':'8', 'C4':'7', 'C5':'2',\
							'C6':'4', 'C7':'3', 'C8':'1', 'C9':'6',\
							'D1':'8', 'D2':'2', 'D3':'5', 'D4':'4', 'D5':'3',\
							'D6':'7', 'D7':'1', 'D8':'6', 'D9':'9',\
							'E1':'7', 'E2':'9', 'E3':'1', 'E4':'5', 'E5':'8',\
							'E6':'6', 'E7':'4', 'E8':'3', 'E9':'2',\
							'F1':'3', 'F2':'4', 'F3':'6', 'F4':'9', 'F5':'1',\
							'F6':'2', 'F7':'7', 'F8':'5', 'F9':'8',\
							'G1':'2', 'G2':'8', 'G3':'9', 'G4':'6', 'G5':'4',\
							'G6':'3', 'G7':'5', 'G8':'7', 'G9':'1',\
							'H1':'5', 'H2':'7', 'H3':'3', 'H4':'2', 'H5':'9',\
							'H6':'1', 'H7':'6', 'H8':'8', 'H9':'4',\
							'I1':'1', 'I2':'6', 'I3':'4', 'I4':'8', 'I5':'7',\
							'I6':'5', 'I7':'2', 'I8':'9', 'I9':'3'}		

		self.matrix_solved = [ [4, 1, 7, 3, 6, 9, 8, 2, 5],\
								[6, 3, 2, 1, 5, 8, 9, 4, 7],\
								[9, 5, 8, 7, 2, 4, 3, 1, 6],\
								[8, 2, 5, 4, 3, 7, 1, 6, 9],\
								[7, 9, 1, 5, 8, 6, 4, 3, 2],\
								[3, 4, 6, 9, 1, 2, 7, 5, 8],\
								[2, 8, 9, 6, 4, 3, 5, 7, 1],\
								[5, 7, 3, 2, 9, 1, 6, 8, 4],\
								[1, 6, 4, 8, 7, 5, 2, 9, 3] ]	
		self.mtrxhandler_solved = MatrixHandler(self.matrix_solved)
		#---------------------------------------------------------------------
		
	def test_convert_matrix_to_grid(self):
		norvig = Norvig(self.mtrxhandler)
		self.assertEqual(self.grid,norvig._to_grid())
	
	def test_construct_possible_values_grid(self):
		norvig = Norvig(self.mtrxhandler)
		self.assertEqual(self.grid_possible_values,\
							norvig._construct_possible_values_grid(self.grid))
	
	def test_eliminate_false_if_cotradiction_met(self):
		norvig = Norvig(self.mtrxhandler)
		self.assertFalse(norvig._eliminate(self.grid_contradiction,\
								self.field, self.value_with_contradiction))
	
	def test_eliminate_value_if_valid(self):
		norvig = Norvig(self.mtrxhandler)
		actual = norvig._eliminate(self.grid_possible_values, self.field,\
							self.value_valid)[self.field]
		self.assertTrue(self.value_valid not in actual)

	def test_assign_false_if_cotradiction_met(self):
		norvig = Norvig(self.mtrxhandler)
		self.assertFalse(norvig._assign(self.grid, self.field,\
							self.value_with_contradiction))
	
	def test_assign_value_if_valid(self):
		norvig = Norvig(self.mtrxhandler)
		expected = self.value_valid
		actual = norvig._assign(self.grid_possible_values, self.field,\
							self.value_valid)[self.field]
		self.assertEqual(expected, actual)
	
	def test_search(self):
		norvig = Norvig(self.mtrxhandler)
		self.assertEqual(self.grid_solved,\
							norvig._search(self.grid_possible_values))
	
	def test_solve(self):
		norvig = Norvig(self.mtrxhandler)
		self.assertEqual(self.mtrxhandler_solved.first_matrix,\
							norvig.solve().first_matrix)

	def test_solve_unsolvable_casemultiple(self):
		norvig = Norvig(self.mtrxhandler_multiple)
		self.assertEqual(None, norvig.solve())

	def test_solve_unsolvable_caseunsolvable(self):
		norvig = Norvig(self.mtrxhandler_unsolvable)
		self.assertEqual(None, norvig.solve())


if __name__ == "__main__":
	unittest.main()
