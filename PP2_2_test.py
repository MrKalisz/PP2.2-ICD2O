import os.path
import sys
import PP2_2

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: -ives\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: 10 is positive\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: -eys\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "In:\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: -s\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: -3 is negative\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: -ies\n"

def test_q2_4(capsys):

	try:
		exists = os.path.exists("PP2_2.py")
		assert exists
	except:
		sys.exit()

	PP2_2.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: 5 is positive\n"

