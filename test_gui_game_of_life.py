import pytest
from unittest.mock import patch
from io import StringIO
import sys
from gui_game_of_life import GameOfLife

@pytest.fixture
def game_instance():
    return GameOfLife()

def test_init(game_instance):
    assert game_instance.how_many_iterations == 0
    assert len(game_instance.how_many_alive) == 1
    assert game_instance.how_many_alive[0] == game_instance.chech_how_many_alive()

def test_show_board(game_instance, capsys):
    game_instance.show_board()
    captured = capsys.readouterr()
    assert "Show Board" in captured.out

def test_end(game_instance, capsys):
    with patch.object(sys, 'exit') as mock_exit:
        game_instance.end()
        mock_exit.assert_called_once_with()

def test_make_a_plot(game_instance):
    with patch("matplotlib.pyplot.show") as mock_show:
        game_instance.make_a_plot()
        mock_show.assert_called_once()

def test_how_many_neighbours(game_instance):
    game_instance.board = [["0", "0", "."], ["0", ".", "0"], [".", ".", "."]]
    assert game_instance.how_many_neighbours(0, 0) == 3
    assert game_instance.how_many_neighbours(1, 1) == 8
    assert game_instance.how_many_neighbours(2, 2) == 0

def test_chech_how_many_alive(game_instance):
    game_instance.board = [["0", ".", "."], [".", "0", "."], [".", ".", "."]]
    assert game_instance.chech_how_many_alive() == 2

def test_one_iteration(game_instance):
    initial_alive_cells = game_instance.chech_how_many_alive()
    game_instance.one_iteration()
    final_alive_cells = game_instance.chech_how_many_alive()
    assert final_alive_cells != initial_alive_cells

def test_do_one_iteration(game_instance, capsys):
    initial_alive_cells = game_instance.chech_how_many_alive()
    game_instance.do_one_iteration()
    final_alive_cells = game_instance.chech_how_many_alive()
    captured = capsys.readouterr()
    assert final_alive_cells != initial_alive_cells
    assert "Show Board" in captured.out

def test_draw_board(game_instance):
    with patch("tkinter.Canvas.create_rectangle") as mock_create_rectangle:
        game_instance.draw_board()
        mock_create_rectangle.assert_called_once()

def test_run_gui(game_instance):
    with patch("tkinter.Tk.mainloop") as mock_mainloop:
        game_instance.run_gui()
        mock_mainloop.assert_called_once()