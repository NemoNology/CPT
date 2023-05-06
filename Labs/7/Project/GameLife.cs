using System;
using System.Collections.Generic;

namespace Project
{
    internal class GameLife
    { 
        private readonly int _gameSize;
        private bool[,] _zone;

        /// <summary>
        /// Size if game zone/field
        /// </summary>
        public int GameSize => _gameSize;

        /// <summary>
        /// Copy of game zone/field
        /// </summary>
        public bool[,] Zone => (bool[,])_zone.Clone();

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
            if (gameSize < 0)
            {
                throw new ArgumentOutOfRangeException(nameof(gameSize));
            }

            _gameSize = gameSize;
            _zone = new bool[gameSize + 2, gameSize + 2];
        }

        /// <summary>
        /// Calculate new values for cells in zone <br/>
        /// <i> Make cells live or dead </i>
        /// </summary>
        public void Move()
        {
            var changes = new List<(int x, int y, bool newValue)>();

            for (int y = 1; y <= _gameSize; y++)
            {
                for (int x = 1; x <= _gameSize; x++)
                {
                    var neighborsAmount = CalculateNeighbors(x, y);
                    var isCellLive = _zone[y, x];

                    // Rules
                    if (!isCellLive && neighborsAmount == 3)
                    {
                        changes.Add(new(x - 1, y - 1, true));
                    }
                    else if (isCellLive &&
                        (neighborsAmount < 2 || neighborsAmount > 3))
                    {
                        changes.Add(new(x - 1, y - 1, false));
                    }
                }
            }

            Changes?.Invoke(changes);

            foreach (var change in changes)
            {
                _zone[change.y, change.x] = change.newValue;
            }
        }

        /// <summary>
        /// Fill game zone/field with live or dead cells - randomly
        /// </summary>
        public void RandomFilling()
        {
            var rnd = new Random(DateTime.Now.Millisecond);
            var changes = new List<(int x, int y, bool newValue)>();

            for (int y = 1; y <= _gameSize; y++)
            {
                for (int x = 1; x <= _gameSize; x++)
                {
                    if (rnd.Next(5) > 3)
                    {
                        _zone[y, x] = true;

                        changes.Add(new(x - 1, y - 1, true));
                    }
                    else
                    {
                        _zone[y, x] = false;

                        changes.Add(new(x - 1, y - 1, false));
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

            Changes?.Invoke(new List<(int x, int y, bool newValue)> { (x - 1, y - 1, _zone[y, x]) });
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

            if (y - 1 < 0 ||
                y + 1 >= _zone.GetLength(0) ||
                x - 1 < 0 ||
                x + 1 >= _zone.GetLength(1))
            {
                return res;
            }

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

        /// <summary>
        /// Calculate new values for cells in selected zone <br/>
        /// <i> Make cells in selected zone live or dead </i>
        /// </summary>
        /// <param name="fromX"> Selected zone coordinates start by X axis </param>
        /// <param name="toX"> Selected zone coordinates end (inclusive) by X axis </param>
        /// <param name="fromY"> Selected zone coordinates start by Y axis </param>
        /// <param name="toY"> Selected zone coordinates end (inclusive) by Y axis </param>
        public List<(int x, int y, bool newValue)> MovePart(int fromX, int toX, int fromY, int toY)
        {
            var changes = new List<(int x, int y, bool newValue)>();

            for (int y = fromY; y < toY; y++)
            {
                for (int x = fromX; x < toX; x++)
                {
                    var neighborsAmount = CalculateNeighbors(x, y);
                    var isCellLive = _zone[y, x];

                    // Rules
                    if (!isCellLive && neighborsAmount == 3)
                    {
                        changes.Add(new(x - 1, y - 1, true));
                    }
                    else if (isCellLive &&
                        (neighborsAmount < 2 || neighborsAmount > 3))
                    {
                        changes.Add(new(x - 1, y - 1, false));
                    }
                }
            }

            return changes;
        }
    
        public void ChangeZoneByChangesList(List<(int x, int y, bool newValue)> changes)
        {
            foreach (var change in changes)
            {
                _zone[change.y, change.x] = change.newValue;
            }
        }
    }
}
