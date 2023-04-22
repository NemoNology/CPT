using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using Color = System.Drawing.Color;

namespace Project
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            _gameLife.Changes += RedrawImage;

            mainView.Source = BitmapToImageSource(_mainViewBuffer);

            Task.Factory.StartNew(GameSimulate);
        }

        private const int GameSize = 20;

        private readonly GameLife _gameLife = new(GameSize);
        private readonly Bitmap _mainViewBuffer = new(GameSize, GameSize);

        private bool _isSimulationAlive = false;

        // For locking
        private readonly object _mutex = new();

        /// <summary>
        /// Convert Bitmap to ImageSource <b> [Not Mine] </b>
        /// </summary>
        /// <param name="bitmap"> Bitmap that will be converted </param>
        /// <returns> Converted Bitmap as ImageSource </returns>
        private ImageSource BitmapToImageSource(Bitmap bitmap)
        {
            MemoryStream ms = new ();
            bitmap.Save(ms, System.Drawing.Imaging.ImageFormat.Bmp);
            BitmapImage image = new ();
            image.BeginInit();
            ms.Seek(0, SeekOrigin.Begin);
            image.StreamSource = ms;
            image.EndInit();

            return image;
        }

        /// <summary>
        /// Redraw main view by updated cells values
        /// </summary>
        /// <param name="changes"></param>
        private async void RedrawImage(List<(int x, int y, bool newCellValue)> changes)
        {
            var liveCellColor = Color.White;
            var deadCellColor = Color.Black;

            foreach (var change in changes)
            {
                _mainViewBuffer.SetPixel(change.x, change.y,
                    change.newCellValue ? liveCellColor : deadCellColor);
            }

            
            await Dispatcher.InvokeAsync(() =>
            {
                mainView.Source = BitmapToImageSource(_mainViewBuffer);
            });
        }

        private void RandomizeGameZone_Click(object sender, RoutedEventArgs e)
        {
            _gameLife.RandomFilling();
        }

        private void Stop_Click(object sender, RoutedEventArgs e)
        {
            lock (_mutex)
            {
                _isSimulationAlive = false;
            }
        }

        private void Continue_Click(object sender, RoutedEventArgs e)
        {
            lock (_mutex)
            {
                _isSimulationAlive = true;
            }
        }

        /// <summary>
        /// Additional thread algorithm - game simulation
        /// </summary>
        private async void GameSimulate()
        {
            while (true)
            {
                if (_isSimulationAlive)
                {
                    lock (_mutex)
                    {
                        _gameLife.Move();
                    }
                }

                await Task.Delay(600);
            }
        }

        private void MainView_MouseMove(object sender, System.Windows.Input.MouseEventArgs e)
        {
            var coordinates = e.GetPosition(sender as IInputElement);

            var x = Math.Round(coordinates.X * GameSize / mainView.ActualWidth, 
                MidpointRounding.ToPositiveInfinity);
            var y = Math.Round(coordinates.Y * GameSize / mainView.ActualHeight,
                MidpointRounding.ToPositiveInfinity);

            outputMouseCoordinates.Content = $"{x}, {y}";
        }

        private void MainView_MouseDown(object sender, System.Windows.Input.MouseButtonEventArgs e)
        {
            var coordinates = e.GetPosition(sender as IInputElement);

            var x = Math.Round(coordinates.X * GameSize / mainView.ActualWidth,
                MidpointRounding.ToPositiveInfinity);
            var y = Math.Round(coordinates.Y * GameSize / mainView.ActualHeight,
                MidpointRounding.ToPositiveInfinity);

            lock (_mutex)
            {
                _gameLife.ChangeStateForCell((int)x, (int)y);
            }
        }
    }
}