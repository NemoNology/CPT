﻿using System;
using System.Collections.Generic;

namespace Project
{
    internal class GameLife
    { 
        private int _gameSize = 20;
        private bool[,] _zone;

        /// <summary>
        /// Size if game zone/field
        /// </summary>
        public int GameSize => _gameSize;

        /// <summary>
        /// Event notifying about changes in the state of cells on the game field/zone
        /// </summary>
        public event Action<List<(int x, int y, bool newValue)>>? Changes;

        /// <summary>
        /// Initialize new GameLife object with inputted game zone/field size
        /// </summary>
        /// <param name="gameSize"> Size of game zone/field </param>
        public GameLife(int gameSize = 20)
        {
            _gameSize = gameSize;
            _zone = new bool[gameSize + 2, gameSize + 2];
        }

        /// <summary>
        /// Calculate new values for cells in zone <br/>
        /// <i> Make cells live or dead </i>
        /// </summary>
        public void Move()
        {
            bool[,] buffer = new bool[_gameSize + 2, _gameSize + 2];
            var changes = new List<(int x, int y, bool newValue)>();

            for (int y = 1; y < _gameSize + 1; y++)
            {
                for (int x = 1; x < _gameSize + 1; x++)
                {
                    var neighborsAmount = CalculateNeighbors(x, y);
                    var isCellLive = _zone[y, x];

                    // Rules
                    if (!isCellLive && neighborsAmount == 3)
                    {
                        buffer[y, x] = true;

                        changes.Add(new(x - 1, y - 1, true));
                    }
                    else if (isCellLive &&
                        (neighborsAmount < 2 || neighborsAmount > 3))
                    {
                        buffer[y, x] = false;

                        changes.Add(new(x - 1, y - 1, false));
                    }
                }
            }

            Changes?.Invoke(changes);

            _zone = buffer;
        }

        /// <summary>
        /// Fill game zone/field with live or dead cells - randomly
        /// </summary>
        public void RandomFilling()
        {
            var rnd = new Random(DateTime.Now.Millisecond);
            var changes = new List<(int x, int y, bool newValue)>();

            for (int y = 1; y < _gameSize + 1; y++)
            {
                for (int x = 1; x < _gameSize + 1; x++)
                {
                    if (rnd.Next(5) > 3)
                    {
                        _zone[y, x] = true;

                        changes.Add((x, y, true));
                    }
                }
            }

            Changes?.Invoke(changes);
        }

        /// <summary>
        /// Change cell state (Dead to live and vice versa) by inputted coordinates
        /// </summary>
        /// <param name="x"> Cell horizontal/row coordinate </param>
        /// <param name="y"> Cell vertical/column coordinate </param>
        public void ChangeStateForCell(int x, int y)
        {
            _zone[y, x] = !_zone[y, x];
        }

        /// <summary>
        /// Calculate neighbors for cell by inputted coordinates
        /// </summary>
        /// <param name="x"> Cell horizontal/row coordinate </param>
        /// <param name="y"> Cell vertical/column coordinate </param>
        /// <returns> Neighbors amount for cell by inputted coordinates </returns>
        private int CalculateNeighbors(int x, int y)
        {
            int res = 0;

            // Left - Up
            if (_zone[y - 1, x - 1])
            {
                res++;
            }

            // Up
            if (_zone[y - 1, x])
            {
                res++;
            }

            // Right - Up
            if (_zone[y - 1, x + 1])
            {
                res++;
            }

            // Left
            if (_zone[y, x - 1])
            {
                res++;
            }

            // Right
            if (_zone[y, x + 1])
            {
                res++;
            }

            // Left - Down
            if (_zone[y + 1, x - 1])
            {
                res++;
            }

            // Down
            if (_zone[y + 1, x])
            {
                res++;
            }

            // Right - Down
            if (_zone[y + 1, x + 1])
            {
                res++;
            }

            return res;
        }
    }
}
