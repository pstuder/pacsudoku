import unittest
from itertools import product
from solver import Algorithm, Norvig, XAlgorithm, Backtracking
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

class TestXAlgorithm(unittest.TestCase):
	def setUp(self):
		self.matrix=[[4, 0, 0, 0, 0, 0, 8, 0, 5],\
                        [0, 3, 0, 0, 0, 0, 0, 0, 0],\
                        [0, 0, 0, 7, 0, 0, 0, 0, 0],\
                        [0, 2, 0, 0, 0, 0, 0, 6, 0],\
                        [0, 0, 0, 0, 8, 0, 4, 0, 0],\
                        [0, 0, 0, 0, 1, 0, 0, 0, 0],\
                        [0, 0, 0, 6, 0, 3, 0, 7, 0],\
                        [5, 0, 0, 2, 0, 0, 0, 0, 0],\
                        [1, 0, 4, 0, 0, 0, 0, 0, 0]]
		self.mtrxhandler = MatrixHandler(self.matrix)
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
		self.create_x_values=[('rc', (0, 0)), ('rc', (0, 1)), ('rc', (0, 2)), ('rc', (0, 3)), ('rc', (0, 4)), ('rc', (0, 5)), ('rc', (0, 6)), ('rc', (0, 7)), ('rc', (0, 8)),\
                              ('rc', (1, 0)), ('rc', (1, 1)), ('rc', (1, 2)), ('rc', (1, 3)), ('rc', (1, 4)), ('rc', (1, 5)), ('rc', (1, 6)), ('rc', (1, 7)), ('rc', (1, 8)),\
                              ('rc', (2, 0)), ('rc', (2, 1)), ('rc', (2, 2)), ('rc', (2, 3)), ('rc', (2, 4)), ('rc', (2, 5)), ('rc', (2, 6)), ('rc', (2, 7)), ('rc', (2, 8)),\
                              ('rc', (3, 0)), ('rc', (3, 1)), ('rc', (3, 2)), ('rc', (3, 3)), ('rc', (3, 4)), ('rc', (3, 5)), ('rc', (3, 6)), ('rc', (3, 7)), ('rc', (3, 8)),\
                              ('rc', (4, 0)), ('rc', (4, 1)), ('rc', (4, 2)), ('rc', (4, 3)), ('rc', (4, 4)), ('rc', (4, 5)), ('rc', (4, 6)), ('rc', (4, 7)), ('rc', (4, 8)),\
                              ('rc', (5, 0)), ('rc', (5, 1)), ('rc', (5, 2)), ('rc', (5, 3)), ('rc', (5, 4)), ('rc', (5, 5)), ('rc', (5, 6)), ('rc', (5, 7)), ('rc', (5, 8)),\
                              ('rc', (6, 0)), ('rc', (6, 1)), ('rc', (6, 2)), ('rc', (6, 3)), ('rc', (6, 4)), ('rc', (6, 5)), ('rc', (6, 6)), ('rc', (6, 7)), ('rc', (6, 8)),\
                              ('rc', (7, 0)), ('rc', (7, 1)), ('rc', (7, 2)), ('rc', (7, 3)), ('rc', (7, 4)), ('rc', (7, 5)), ('rc', (7, 6)), ('rc', (7, 7)), ('rc', (7, 8)),\
                              ('rc', (8, 0)), ('rc', (8, 1)), ('rc', (8, 2)), ('rc', (8, 3)), ('rc', (8, 4)), ('rc', (8, 5)), ('rc', (8, 6)), ('rc', (8, 7)), ('rc', (8, 8)),\
                              ('rn', (0, 1)), ('rn', (0, 2)), ('rn', (0, 3)), ('rn', (0, 4)), ('rn', (0, 5)), ('rn', (0, 6)), ('rn', (0, 7)), ('rn', (0, 8)), ('rn', (0, 9)),\
                              ('rn', (1, 1)), ('rn', (1, 2)), ('rn', (1, 3)), ('rn', (1, 4)), ('rn', (1, 5)), ('rn', (1, 6)), ('rn', (1, 7)), ('rn', (1, 8)), ('rn', (1, 9)),\
                              ('rn', (2, 1)), ('rn', (2, 2)), ('rn', (2, 3)), ('rn', (2, 4)), ('rn', (2, 5)), ('rn', (2, 6)), ('rn', (2, 7)), ('rn', (2, 8)), ('rn', (2, 9)),\
                              ('rn', (3, 1)), ('rn', (3, 2)), ('rn', (3, 3)), ('rn', (3, 4)), ('rn', (3, 5)), ('rn', (3, 6)), ('rn', (3, 7)), ('rn', (3, 8)), ('rn', (3, 9)),\
                              ('rn', (4, 1)), ('rn', (4, 2)), ('rn', (4, 3)), ('rn', (4, 4)), ('rn', (4, 5)), ('rn', (4, 6)), ('rn', (4, 7)), ('rn', (4, 8)), ('rn', (4, 9)),\
                              ('rn', (5, 1)), ('rn', (5, 2)), ('rn', (5, 3)), ('rn', (5, 4)), ('rn', (5, 5)), ('rn', (5, 6)), ('rn', (5, 7)), ('rn', (5, 8)), ('rn', (5, 9)),\
                              ('rn', (6, 1)), ('rn', (6, 2)), ('rn', (6, 3)), ('rn', (6, 4)), ('rn', (6, 5)), ('rn', (6, 6)), ('rn', (6, 7)), ('rn', (6, 8)), ('rn', (6, 9)),\
                              ('rn', (7, 1)), ('rn', (7, 2)), ('rn', (7, 3)), ('rn', (7, 4)), ('rn', (7, 5)), ('rn', (7, 6)), ('rn', (7, 7)), ('rn', (7, 8)), ('rn', (7, 9)),\
                              ('rn', (8, 1)), ('rn', (8, 2)), ('rn', (8, 3)), ('rn', (8, 4)), ('rn', (8, 5)), ('rn', (8, 6)), ('rn', (8, 7)), ('rn', (8, 8)), ('rn', (8, 9)),\
                              ('cn', (0, 1)), ('cn', (0, 2)), ('cn', (0, 3)), ('cn', (0, 4)), ('cn', (0, 5)), ('cn', (0, 6)), ('cn', (0, 7)), ('cn', (0, 8)), ('cn', (0, 9)),\
                              ('cn', (1, 1)), ('cn', (1, 2)), ('cn', (1, 3)), ('cn', (1, 4)), ('cn', (1, 5)), ('cn', (1, 6)), ('cn', (1, 7)), ('cn', (1, 8)), ('cn', (1, 9)),\
                              ('cn', (2, 1)), ('cn', (2, 2)), ('cn', (2, 3)), ('cn', (2, 4)), ('cn', (2, 5)), ('cn', (2, 6)), ('cn', (2, 7)), ('cn', (2, 8)), ('cn', (2, 9)),\
                              ('cn', (3, 1)), ('cn', (3, 2)), ('cn', (3, 3)), ('cn', (3, 4)), ('cn', (3, 5)), ('cn', (3, 6)), ('cn', (3, 7)), ('cn', (3, 8)), ('cn', (3, 9)),\
                              ('cn', (4, 1)), ('cn', (4, 2)), ('cn', (4, 3)), ('cn', (4, 4)), ('cn', (4, 5)), ('cn', (4, 6)), ('cn', (4, 7)), ('cn', (4, 8)), ('cn', (4, 9)),\
                              ('cn', (5, 1)), ('cn', (5, 2)), ('cn', (5, 3)), ('cn', (5, 4)), ('cn', (5, 5)), ('cn', (5, 6)), ('cn', (5, 7)), ('cn', (5, 8)), ('cn', (5, 9)),\
                              ('cn', (6, 1)), ('cn', (6, 2)), ('cn', (6, 3)), ('cn', (6, 4)), ('cn', (6, 5)), ('cn', (6, 6)), ('cn', (6, 7)), ('cn', (6, 8)), ('cn', (6, 9)),\
                              ('cn', (7, 1)), ('cn', (7, 2)), ('cn', (7, 3)), ('cn', (7, 4)), ('cn', (7, 5)), ('cn', (7, 6)), ('cn', (7, 7)), ('cn', (7, 8)), ('cn', (7, 9)),\
                              ('cn', (8, 1)), ('cn', (8, 2)), ('cn', (8, 3)), ('cn', (8, 4)), ('cn', (8, 5)), ('cn', (8, 6)), ('cn', (8, 7)), ('cn', (8, 8)), ('cn', (8, 9)),\
                              ('bn', (0, 1)), ('bn', (0, 2)), ('bn', (0, 3)), ('bn', (0, 4)), ('bn', (0, 5)), ('bn', (0, 6)), ('bn', (0, 7)), ('bn', (0, 8)), ('bn', (0, 9)),\
                              ('bn', (1, 1)), ('bn', (1, 2)), ('bn', (1, 3)), ('bn', (1, 4)), ('bn', (1, 5)), ('bn', (1, 6)), ('bn', (1, 7)), ('bn', (1, 8)), ('bn', (1, 9)),\
                              ('bn', (2, 1)), ('bn', (2, 2)), ('bn', (2, 3)), ('bn', (2, 4)), ('bn', (2, 5)), ('bn', (2, 6)), ('bn', (2, 7)), ('bn', (2, 8)), ('bn', (2, 9)),\
                              ('bn', (3, 1)), ('bn', (3, 2)), ('bn', (3, 3)), ('bn', (3, 4)), ('bn', (3, 5)), ('bn', (3, 6)), ('bn', (3, 7)), ('bn', (3, 8)), ('bn', (3, 9)),\
                              ('bn', (4, 1)), ('bn', (4, 2)), ('bn', (4, 3)), ('bn', (4, 4)), ('bn', (4, 5)), ('bn', (4, 6)), ('bn', (4, 7)), ('bn', (4, 8)), ('bn', (4, 9)),\
                              ('bn', (5, 1)), ('bn', (5, 2)), ('bn', (5, 3)), ('bn', (5, 4)), ('bn', (5, 5)), ('bn', (5, 6)), ('bn', (5, 7)), ('bn', (5, 8)), ('bn', (5, 9)),\
                              ('bn', (6, 1)), ('bn', (6, 2)), ('bn', (6, 3)), ('bn', (6, 4)), ('bn', (6, 5)), ('bn', (6, 6)), ('bn', (6, 7)), ('bn', (6, 8)), ('bn', (6, 9)),\
                              ('bn', (7, 1)), ('bn', (7, 2)), ('bn', (7, 3)), ('bn', (7, 4)), ('bn', (7, 5)), ('bn', (7, 6)), ('bn', (7, 7)), ('bn', (7, 8)), ('bn', (7, 9)),\
                              ('bn', (8, 1)), ('bn', (8, 2)), ('bn', (8, 3)), ('bn', (8, 4)), ('bn', (8, 5)), ('bn', (8, 6)), ('bn', (8, 7)), ('bn', (8, 8)), ('bn', (8, 9))]

		self.create_wrong_x_values=[('rc', (0, 9)), ('rc', (0, 1)), ('rc', (0, 2)), ('rc', (0, 3)), ('rc', (0, 4)), ('rc', (0, 5)), ('rc', (0, 6)), ('rc', (0, 7)), ('rc', (0, 8)),\
                              ('rc', (1, 0)), ('rc', (1, 1)), ('rc', (1, 2)), ('rc', (1, 3)), ('rc', (1, 4)), ('rc', (1, 5)), ('rc', (1, 6)), ('rc', (1, 7)), ('rc', (1, 8)),\
                              ('rc', (2, 0)), ('rc', (2, 1)), ('rc', (2, 2)), ('rc', (2, 3)), ('rc', (2, 4)), ('rc', (2, 5)), ('rc', (2, 6)), ('rc', (2, 7)), ('rc', (2, 8)),\
                              ('rc', (3, 0)), ('rc', (3, 1)), ('rc', (3, 2)), ('rc', (3, 3)), ('rc', (3, 4)), ('rc', (3, 5)), ('rc', (3, 6)), ('rc', (3, 7)), ('rc', (3, 8)),\
                              ('rc', (4, 0)), ('rc', (4, 1)), ('rc', (4, 2)), ('rc', (4, 3)), ('rc', (4, 4)), ('rc', (4, 5)), ('rc', (4, 6)), ('rc', (4, 7)), ('rc', (4, 8)),\
                              ('rc', (5, 0)), ('rc', (5, 1)), ('rc', (5, 2)), ('rc', (5, 3)), ('rc', (5, 4)), ('rc', (5, 5)), ('rc', (5, 6)), ('rc', (5, 7)), ('rc', (5, 8)),\
                              ('rc', (6, 0)), ('rc', (6, 1)), ('rc', (6, 2)), ('rc', (6, 3)), ('rc', (6, 4)), ('rc', (6, 5)), ('rc', (6, 6)), ('rc', (6, 7)), ('rc', (6, 8)),\
                              ('rc', (7, 0)), ('rc', (7, 1)), ('rc', (7, 2)), ('rc', (7, 3)), ('rc', (7, 4)), ('rc', (7, 5)), ('rc', (7, 6)), ('rc', (7, 7)), ('rc', (7, 8)),\
                              ('rc', (8, 0)), ('rc', (8, 1)), ('rc', (8, 2)), ('rc', (8, 3)), ('rc', (8, 4)), ('rc', (8, 5)), ('rc', (8, 6)), ('rc', (8, 7)), ('rc', (8, 8)),\
                              ('rn', (0, 1)), ('rn', (0, 2)), ('rn', (0, 3)), ('rn', (0, 4)), ('rn', (0, 5)), ('rn', (0, 6)), ('rn', (0, 7)), ('rn', (0, 8)), ('rn', (0, 9)),\
                              ('rn', (1, 1)), ('rn', (1, 2)), ('rn', (1, 3)), ('rn', (1, 4)), ('rn', (1, 5)), ('rn', (1, 6)), ('rn', (1, 7)), ('rn', (1, 8)), ('rn', (1, 9)),\
                              ('rn', (2, 1)), ('rn', (2, 2)), ('rn', (2, 3)), ('rn', (2, 4)), ('rn', (2, 5)), ('rn', (2, 6)), ('rn', (2, 7)), ('rn', (2, 8)), ('rn', (2, 9)),\
                              ('rn', (3, 1)), ('rn', (3, 2)), ('rn', (3, 3)), ('rn', (3, 4)), ('rn', (3, 5)), ('rn', (3, 6)), ('rn', (3, 7)), ('rn', (3, 8)), ('rn', (3, 9)),\
                              ('rn', (4, 1)), ('rn', (4, 2)), ('rn', (4, 3)), ('rn', (4, 4)), ('rn', (4, 5)), ('rn', (4, 6)), ('rn', (4, 7)), ('rn', (4, 8)), ('rn', (4, 9)),\
                              ('rn', (5, 1)), ('rn', (5, 2)), ('rn', (5, 3)), ('rn', (5, 4)), ('rn', (5, 5)), ('rn', (5, 6)), ('rn', (5, 7)), ('rn', (5, 8)), ('rn', (5, 9)),\
                              ('rn', (6, 1)), ('rn', (6, 2)), ('rn', (6, 3)), ('rn', (6, 4)), ('rn', (6, 5)), ('rn', (6, 6)), ('rn', (6, 7)), ('rn', (6, 8)), ('rn', (6, 9)),\
                              ('rn', (7, 1)), ('rn', (7, 2)), ('rn', (7, 3)), ('rn', (7, 4)), ('rn', (7, 5)), ('rn', (7, 6)), ('rn', (7, 7)), ('rn', (7, 8)), ('rn', (7, 9)),\
                              ('rn', (8, 1)), ('rn', (8, 2)), ('rn', (8, 3)), ('rn', (8, 4)), ('rn', (8, 5)), ('rn', (8, 6)), ('rn', (8, 7)), ('rn', (8, 8)), ('rn', (8, 9)),\
                              ('cn', (0, 1)), ('cn', (0, 2)), ('cn', (0, 3)), ('cn', (0, 4)), ('cn', (0, 5)), ('cn', (0, 6)), ('cn', (0, 7)), ('cn', (0, 8)), ('cn', (0, 9)),\
                              ('cn', (1, 1)), ('cn', (1, 2)), ('cn', (1, 3)), ('cn', (1, 4)), ('cn', (1, 5)), ('cn', (1, 6)), ('cn', (1, 7)), ('cn', (1, 8)), ('cn', (1, 9)),\
                              ('cn', (2, 1)), ('cn', (2, 2)), ('cn', (2, 3)), ('cn', (2, 4)), ('cn', (2, 5)), ('cn', (2, 6)), ('cn', (2, 7)), ('cn', (2, 8)), ('cn', (2, 9)),\
                              ('cn', (3, 1)), ('cn', (3, 2)), ('cn', (3, 3)), ('cn', (3, 4)), ('cn', (3, 5)), ('cn', (3, 6)), ('cn', (3, 7)), ('cn', (3, 8)), ('cn', (3, 9)),\
                              ('cn', (4, 1)), ('cn', (4, 2)), ('cn', (4, 3)), ('cn', (4, 4)), ('cn', (4, 5)), ('cn', (4, 6)), ('cn', (4, 7)), ('cn', (4, 8)), ('cn', (4, 9)),\
                              ('cn', (5, 1)), ('cn', (5, 2)), ('cn', (5, 3)), ('cn', (5, 4)), ('cn', (5, 5)), ('cn', (5, 6)), ('cn', (5, 7)), ('cn', (5, 8)), ('cn', (5, 9)),\
                              ('cn', (6, 1)), ('cn', (6, 2)), ('cn', (6, 3)), ('cn', (6, 4)), ('cn', (6, 5)), ('cn', (6, 6)), ('cn', (6, 7)), ('cn', (6, 8)), ('cn', (6, 9)),\
                              ('cn', (7, 1)), ('cn', (7, 2)), ('cn', (7, 3)), ('cn', (7, 4)), ('cn', (7, 5)), ('cn', (7, 6)), ('cn', (7, 7)), ('cn', (7, 8)), ('cn', (7, 9)),\
                              ('cn', (8, 1)), ('cn', (8, 2)), ('cn', (8, 3)), ('cn', (8, 4)), ('cn', (8, 5)), ('cn', (8, 6)), ('cn', (8, 7)), ('cn', (8, 8)), ('cn', (8, 9)),\
                              ('bn', (0, 1)), ('bn', (0, 2)), ('bn', (0, 3)), ('bn', (0, 4)), ('bn', (0, 5)), ('bn', (0, 6)), ('bn', (0, 7)), ('bn', (0, 8)), ('bn', (0, 9)),\
                              ('bn', (1, 1)), ('bn', (1, 2)), ('bn', (1, 3)), ('bn', (1, 4)), ('bn', (1, 5)), ('bn', (1, 6)), ('bn', (1, 7)), ('bn', (1, 8)), ('bn', (1, 9)),\
                              ('bn', (2, 1)), ('bn', (2, 2)), ('bn', (2, 3)), ('bn', (2, 4)), ('bn', (2, 5)), ('bn', (2, 6)), ('bn', (2, 7)), ('bn', (2, 8)), ('bn', (2, 9)),\
                              ('bn', (3, 1)), ('bn', (3, 2)), ('bn', (3, 3)), ('bn', (3, 4)), ('bn', (3, 5)), ('bn', (3, 6)), ('bn', (3, 7)), ('bn', (3, 8)), ('bn', (3, 9)),\
                              ('bn', (4, 1)), ('bn', (4, 2)), ('bn', (4, 3)), ('bn', (4, 4)), ('bn', (4, 5)), ('bn', (4, 6)), ('bn', (4, 7)), ('bn', (4, 8)), ('bn', (4, 9)),\
                              ('bn', (5, 1)), ('bn', (5, 2)), ('bn', (5, 3)), ('bn', (5, 4)), ('bn', (5, 5)), ('bn', (5, 6)), ('bn', (5, 7)), ('bn', (5, 8)), ('bn', (5, 9)),\
                              ('bn', (6, 1)), ('bn', (6, 2)), ('bn', (6, 3)), ('bn', (6, 4)), ('bn', (6, 5)), ('bn', (6, 6)), ('bn', (6, 7)), ('bn', (6, 8)), ('bn', (6, 9)),\
                              ('bn', (7, 1)), ('bn', (7, 2)), ('bn', (7, 3)), ('bn', (7, 4)), ('bn', (7, 5)), ('bn', (7, 6)), ('bn', (7, 7)), ('bn', (7, 8)), ('bn', (7, 9)),\
                              ('bn', (8, 1)), ('bn', (8, 2)), ('bn', (8, 3)), ('bn', (8, 4)), ('bn', (8, 5)), ('bn', (8, 6)), ('bn', (8, 7)), ('bn', (8, 8)), ('bn', (8, 9))]

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


	def test_solve(self):
		x_algorithm = XAlgorithm(self.mtrxhandler)
		self.assertEqual(self.mtrxhandler_solved.first_matrix, x_algorithm.solve().first_matrix)

	def test_costruct_x_create_a_correct_X_list(self):
		x_algorithm = XAlgorithm(self.mtrxhandler)
		actual_value=x_algorithm.costruct_x(9)
		self.assertEqual(actual_value,self.create_x_values)
	
	
		
	def test_if_does_not_costruct_wrong_x_list_values(self):
		x_algorithm = XAlgorithm(self.mtrxhandler)
		actual_value=x_algorithm.costruct_x(9)
		self.assertNotEqual(actual_value,self.create_wrong_x_values)
		

	def test_solve_unsolvable_casemultiple_XAlgorithm(self):
		x_algorithm = XAlgorithm(self.mtrxhandler_multiple)
		self.assertEqual(None, x_algorithm.solve())

	def test_solve_unsolvable_caseunsolvable_XAlgorithm(self):
		x_algorithm1 = XAlgorithm(self.mtrxhandler_unsolvable)
		self.assertEqual(None, x_algorithm1.solve())

	def test_solve_sudoku_unsolvable_caseunsolvable_XAlgorithm(self):
		x_algorithm1 = XAlgorithm(self.mtrxhandler_unsolvable)
		self.assertEqual(None, x_algorithm1.solve_sudoku((3,3)))	
	
	def test_costruct_y_create_a_correct_y_list(self):
		Row, Column = 3,3
		matrix_lenght = Row * Column
		list_of_X=self.create_x_values
		list_of_Y = dict()
		expected_result=costructy(matrix_lenght,Row,Column,list_of_Y)
		x_algorithm1 = XAlgorithm(self.mtrxhandler_unsolvable)
		actual_result=x_algorithm1.costruct_y(matrix_lenght,Row,Column,list_of_Y)
		self.assertEqual(expected_result,actual_result)

	def test_first_list(self):
		expected_result=gen_list("rc",9,0,9)
		x_algorithm1 = XAlgorithm(self.mtrxhandler_unsolvable)
		actual_result=x_algorithm1.first_list("rc",9,0,9)
		self.assertEqual(expected_result,actual_result)	

def costructy(matrix_lenght,Row,Column,Y):
	for row, column, lenght in product(range(matrix_lenght), range(matrix_lenght), range(1, matrix_lenght + 1)):
		b = (row // Row) * Row + (column // Column) # Box number
		Y[(row, column, lenght)] =[("rc", (row, column)),("rn", (row, lenght)), ("cn", (column, lenght)), ("bn", (b, lenght))]
	return Y

def gen_list(text,matrix_lenght1,start,matrix_lenght2):
	list=[]
	for rc in product(range(matrix_lenght1), range(start,matrix_lenght2)):
		list.append((text, rc))
	return list


class TestBacktrackingAlgorithm(unittest.TestCase):
	
	def setUp(self):
		
		self.input_matrix=[[0,0,0,9,0,0,0,0,6],\
						[5,0,0,0,0,0,0,0,9],\
						[0,4,0,0,0,0,1,0,0],\
						[0,0,6,0,3,1,9,0,8],\
						[2,0,0,5,0,9,0,0,7],\
						[8,0,3,7,4,0,2,0,0],\
						[0,0,8,0,0,0,0,5,0],\
						[9,0,0,0,0,0,0,0,4],\
						[6,0,0,0,0,5,0,0,0]]
		
		self.solved_matrix = [[1, 8, 7, 9, 2, 4, 5, 3, 6],\
							[5, 6, 2, 8, 1, 3, 4, 7, 9],\
							[3, 4, 9, 6, 5, 7, 1, 8, 2],\
							[7, 5, 6, 2, 3, 1, 9, 4, 8],\
							[2, 1, 4, 5, 8, 9, 3, 6, 7],\
							[8, 9, 3, 7, 4, 6, 2, 1, 5],\
							[4, 7, 8, 3, 9, 2, 6, 5, 1],\
							[9, 3, 5, 1, 6, 8, 7, 2, 4],\
							[6, 2, 1, 4, 7, 5, 8, 9, 3]]
		
		self.unsolved_matrix = [[1,2,3,4,5,6,7,8,0],\
							[0,0,0,0,0,0,0,0,2],\
							[0,9,0,1,0,0,0,0,3],\
							[0,0,0,0,0,0,0,0,4],\
							[0,0,0,0,7,0,0,0,5],\
							[0,0,0,0,0,0,0,0,6],\
							[0,0,0,0,1,0,0,0,7],\
							[0,0,1,0,0,2,0,0,8],\
							[0,0,0,0,0,0,0,0,9]]	
	
		self.mtrx_to_solve = MatrixHandler(self.input_matrix)
		self.mtrx_solved = MatrixHandler(self.solved_matrix)
		self.mtrx_unsolved = MatrixHandler(self.unsolved_matrix )

	def test_solve_matrix_return_a_solved_sudoku(self):
		backtracking = Backtracking(self.mtrx_to_solve)
		solved_sudoku_matrix = backtracking.solve().first_matrix
		self.assertEqual(self.mtrx_solved.first_matrix, solved_sudoku_matrix)

	def test_solve_Backtracking_return_True_if_sudoku_is_solved(self):
		backtracking = Backtracking(self.mtrx_to_solve)
		solved_sudoku_correct = backtracking.solve_backtracking()
		self.assertEqual = (True, solved_sudoku_correct)
	
	def test_solve_Backtracking_return_False_if_sudoku_is_not_solved(self):
		backtracking = Backtracking(self.mtrx_unsolved)
		solved_sudoku_correct = backtracking.solve_backtracking()
		self.assertFalse = (solved_sudoku_correct)
	
	def test_solve_sudoku_with_Bactracking_return_None_if_sudoku_is_not_solved(self):
		backtracking = Backtracking(self.mtrx_unsolved)
		solved_sudoku_not_correct = backtracking.solve()
		self.assertEqual(None,solved_sudoku_not_correct)
	
	def test_coordenates_returned_from_first_empty_location_found(self):
		backtracking = Backtracking(self.mtrx_to_solve)
		coordenates_empty_location = backtracking.findunassignedlocation(0,0)
		x =  coordenates_empty_location[1]
		y = coordenates_empty_location[2]
		self.assertEqual((0,0),(x,y))

	def test_False_is_returned_if_tentative_number_1_is_not_repeated_in_row_0(self):
		backtracking = Backtracking(self.mtrx_to_solve)
		row_number_valid = backtracking.num_used_in_row(0,1)
		self.assertFalse(row_number_valid)
		
	
	def test_False_is_returned_if_tentative_number_1_is_not_repeated_in_column_1(self):
		backtracking = Backtracking(self.mtrx_to_solve)
		column_number_valid = backtracking.num_used_in_column(0,1)
		self.assertFalse(column_number_valid)
		
	def test_False_is_returned_if_tentative_number_1_is_not_repeated_in_submatrix_0_0(self):
		backtracking = Backtracking(self.mtrx_to_solve)
		submatrix_number_valid = backtracking.num_used_in_submatrix(0,0,1)
		self.assertFalse(submatrix_number_valid)

if __name__ == "__main__":
	unittest.main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                