import os.path
import sys
import PP2_2

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: The number is not Five\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Positive\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Even\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['Hello']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q4()
	captured = capsys.readouterr()
	assert captured.out == 'Type "Hello": The word is Hello\n'

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: The number is Five\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Negative\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['9']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Odd\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['Hello!']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q4()
	captured = capsys.readouterr()
	assert captured.out == 'Type "Hello": The word is not Hello\n'

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: The number is not Five\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Negative\n"

def test_q3_3(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Even\n"

def test_q4_3(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = [' Hello ']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q4()
	captured = capsys.readouterr()
	assert captured.out == 'Type "Hello": The word is not Hello\n'

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: The number is not Five\n"

def test_q2_4(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5.5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Positive\n"

def test_q3_4(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-2']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Even\n"

def test_q4_4(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['hello']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q4()
	captured = capsys.readouterr()
	assert captured.out == 'Type "Hello": The word is not Hello\n'

def test_q2_5(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-12.7']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Negative\n"

def test_q3_5(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-3']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Odd\n"

def test_q4_5(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	input_values = ['Bye']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_2.input = mock_input

	PP2_2.q4()
	captured = capsys.readouterr()
	assert captured.out == 'Type "Hello": The word is not Hello\n'
