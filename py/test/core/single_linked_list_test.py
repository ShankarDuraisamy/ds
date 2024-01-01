import pytest
from src.core.singly_linked_list import Node, LinkedList


@pytest.fixture
def initialize():
	pass


def test_append_when_head_node_is_none():
	ll = LinkedList()
	node = Node(1)
	ll.append(node)
	assert ll.length() == 1
	assert ll.head.data == 1


def test_append_when_head_node_is_not_none():
	node = Node(1)
	ll = LinkedList(node)
	node_2 = Node(2)
	ll.append(node_2)
	assert ll.length() == 2
	assert ll.head.next.data == 2


def test_prepend_when_head_node_is_none():
	ll = LinkedList()
	node = Node(1)
	ll.prepend(node)
	assert ll.length() == 1
	assert ll.head.data == 1


def test_prepend_when_head_node_is_not_none():
	node = Node(1)
	ll = LinkedList(node)
	node_2 = Node(2)
	ll.prepend(node_2)
	assert ll.length() == 2
	assert ll.head.data == 2
