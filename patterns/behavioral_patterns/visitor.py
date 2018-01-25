# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Spy(metaclass=ABCMeta):
	"""
	Шпион - посетитель
	"""

	@abstractmethod
	def visit(self, facility) -> None:
		"""
		Посетить военный объект
		"""
		pass


class MilitaryFacility(metaclass=ABCMeta):
	"""
	Военный объект - посещаемый объект
	"""

	@abstractmethod
	def accept(self, spy: Spy) -> None:
		"""
		Принять шпиона-посетителя
		"""
		pass


class MilitaryBase(MilitaryFacility):
	"""
	Военная база подводного флота
	"""

	def __init__(self) -> None:
		self._secret_draftings = 1
		self._nuclear_submarines = 1

	def __repr__(self) -> str:
		return 'На военной базе находится {} атомных подводных лодок и {} секретных чертежей'.format(
			self._nuclear_submarines, self._secret_draftings
		)
	
	def accept(self, spy: Spy) -> None:
		spy.visit(self)

	def remove_secret_draftings(self) -> None:
		if self._secret_draftings:
			self._secret_draftings -= 1

	def remove_nuclear_submarine(self) -> None:
		if self._nuclear_submarines:
			self._nuclear_submarines -= 1


class Headquarters(MilitaryFacility):
	"""
	Центральный штаб армии
	"""

	def __init__(self) -> None:
		self._generals = 3
		self._secret_documents = 2

	def __repr__(self) -> str:
		return 'В штабе находится {} генералов и {} секретных документов'.format(
			self._generals, self._secret_documents
		)
	
	def accept(self, spy: Spy) -> None:
		spy.visit(self)

	def remove_general(self) -> None:
		if self._generals:
			self._generals -= 1

	def remove_secret_documents(self) -> None:
		if self._secret_documents:
			self._secret_documents -= 1

class JamesBond(Spy):
	"""
	Конкретный шпион
	"""

	def visit(self, facility: MilitaryFacility) -> None:
		if isinstance(facility, MilitaryBase):		# Джеймс Бонд посещает военную базу
			facility.remove_secret_draftings()		# похищает секретные чертежи 
			facility.remove_nuclear_submarine()		# и напоследок взрывает атомную подводную лодку
		elif isinstance(facility, Headquarters):	# Джеймс Бонд посещает штаб
			facility.remove_general()				# ...
			facility.remove_general()				# ...
			facility.remove_secret_documents()		# ...
			facility.remove_general()				# последовтельно уничтожает всех генералов
			facility.remove_secret_documents()		# и похищает все секретные документы


if __name__ == '__main__':
	base = MilitaryBase()
	hq = Headquarters()
	spy = JamesBond()
	base.accept(spy)
	hq.accept(spy)
	print('OUTPUT:')	# посещения Джеймса Бонда были действительно разрушительными
	print(base)
	print(hq)
