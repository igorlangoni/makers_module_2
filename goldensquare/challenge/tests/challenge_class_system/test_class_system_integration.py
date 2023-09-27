from lib.challenge_class_system.diary import *
from lib.challenge_class_system.diaryEntry import *
from lib.challenge_class_system.todo_list import *
from lib.challenge_class_system.todo import *
from lib.challenge_class_system.contact import *

def test_adding_two_entries_and_showing_in_list():
    diary = Diary()
    entry1 = DiaryEntry('Title1', 'Contents1')
    entry2 = DiaryEntry('Title2', 'Contents2')
    diary.add(entry1)
    diary.add(entry2)
    actual = diary.show_list()
    assert actual == [entry1, entry2]

def test_given_wpm_and_minutes_returns_best_entry_to_read():
    diary = Diary()
    entry1 = DiaryEntry('Title1', 'Contents1 8 9 10 5 6 7 8 9 10 11')
    entry2 = DiaryEntry('Title2', 'Contents2 two three four five six 7 8 93 24 24 26 27 28 29 30')
    entry3 = DiaryEntry('Title3', 'Contents3 two 3 4 6 7')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    actual = diary.best_entry_to_read(3, 4)
    assert actual == entry1

def test_adds_two_tasks_and_returns_them():
    todo_list = TodoList()
    task1 = Todo('walk dog')
    task2 = Todo('take out trash')
    todo_list.add(task1)
    todo_list.add(task2)
    actual = todo_list.show_tasks()
    assert actual == [task1, task2]

def test_adding_contacts_to_entry_and_showing_them():
    entry1 = DiaryEntry('Title1', 'Contents1')
    contact1 = Contact('Igor', '9738-4773')
    contact2 = Contact('Alline', '9738-3840')
    entry1.add_contact(contact1)
    entry1.add_contact(contact2)
    actual = entry1.show_contacts()
    assert actual == [contact1, contact2]

def test_adding_entries_with_contacts_and_returning_all_contacts():
    diary = Diary()
    entry1 = DiaryEntry('Title1', 'Contents1')
    entry2 = DiaryEntry('Title2', 'Contents2')
    contact1 = Contact('Igor', '9738-4773')
    contact2 = Contact('Alline', '9738-3840')
    contact3 = Contact('Vitor', '4656-1376')
    contact4 = Contact('Ze', '3842-2177')
    diary.add(entry1)
    diary.add(entry2)
    entry1.add_contact(contact1)
    entry1.add_contact(contact2)
    entry2.add_contact(contact3)
    entry2.add_contact(contact4)
    actual = diary.show_all_phone_numbers()
    assert actual == ['9738-4773', '9738-3840', '4656-1376', '3842-2177']
