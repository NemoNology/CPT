using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using Color = System.Drawing.Color;
using Brushes = System.Windows.Media.Brushes;
using Project;
using System.Drawing;

namespace ProjectWPF
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            _gameLife.Changes += RedrawView;

            inputThreadsAmount.Text = "1";

            Task.Factory.StartNew(GameSimulate);
        }

        private const int GameSize = 20;

        private readonly GameLife _gameLife = new(GameSize);
        private readonly Bitmap _mainViewBuffer = new(GameSize, GameSize);

        private bool _isSimulationAlive = false;

        private int _threadsAmount = 1;

        // For locking
        private readonly object _mutex = new();

        /// <summary>
        /// Convert Bitmap to ImageSource <b> [Not Mine] </b>
        /// </summary>
        /// <param name="bitmap"> Bitmap that will be converted </param>
        /// <returns> Converted Bitmap as ImageSource </returns>
        private ImageSource BitmapToImageSource(Bitmap bitmap)
        {
            MemoryStream ms = new();
            bitmap.Save(ms, System.Drawing.Imaging.ImageFormat.Bmp);
            BitmapImage image = new();
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
        private async void RedrawView(List<(int x, int y, bool newCellValue)> changes)
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
                outputView.Source = BitmapToImageSource(_mainViewBuffer);
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
            var changes = new List<(int x, int y, bool newCellValue)>();
            Task<List<(int x, int y, bool newCellValue)>>[] tasksPool;

            var liveCellColor = Color.White;
            var deadCellColor = Color.Black;

            // TODO: Out of Range Exception

            while (true)
            {
                if (_isSimulationAlive)
                {
                    tasksPool = new Task<List<(int x, int y, bool newCellValue)>>[_threadsAmount];
                    var partSize = GameSize / _threadsAmount;
                    var isEven = _threadsAmount % 2 == 0;

                    for (int i = 0; i <= _threadsAmount - 1; i++)
                    {
                        if (isEven)
                        {
                            if (i < partSize % _threadsAmount)
                            {
                                tasksPool[i] = Task.Factory.StartNew(() =>
                                    _gameLife.MovePart(
                                        i * partSize + 1,
                                        (i + 2) * partSize + 1,
                                        i * partSize + 1,
                                        (i + 2) * partSize + 1)
                                );

                                i++;
                            }
                            else
                            {
                                tasksPool[i] = Task.Factory.StartNew(() =>
                                    _gameLife.MovePart(
                                        i * partSize + 1,
                                        (i + 1) * partSize + 1,
                                        i * partSize + 1,
                                        (i + 1) * partSize + 1)
                                );
                            }

                        }
                        else
                        {
                            if (i < partSize % _threadsAmount)
                            {
                                tasksPool[i] = Task.Factory.StartNew(() =>
                                    _gameLife.MovePart(
                                        i * partSize + 1,
                                        (i + 2) * partSize + 1,
                                        1, GameSize + 1)
                                );

                                i++;
                            }
                            else
                            {
                                tasksPool[i] = Task.Factory.StartNew(() =>
                                    _gameLife.MovePart(
                                        i * partSize + 1,
                                        (i + 1) * partSize + 1,
                                        1, GameSize + 1)
                                );
                            }
                        }
                    }
                    
                    await Task.WhenAll(tasksPool);

                    foreach (var task in tasksPool)
                    {
                        changes.AddRange(task.Result);

                        foreach (var (x, y, newCellValue) in changes)
                        {
                            _mainViewBuffer.SetPixel(x, y,
                                newCellValue ? liveCellColor : deadCellColor);
                        }
                    }

                    await Dispatcher.InvokeAsync(() =>
                    {
                        outputView.Source = BitmapToImageSource(_mainViewBuffer);
                    });
                }

                // Synchronization
                lock (_mutex)
                {
                    _gameLife.ChangeZoneByChangesList(changes);
                }

                changes.Clear();

                await Task.Delay(500);
            }
        }

        private void ViewInit()
        {
            
        }

        private void InputThreadsAmount_TextChanged(object sender, System.Windows.Controls.TextChangedEventArgs e)
        {
            if (inputThreadsAmount == null)
            {
                return;
            }

            lock (_mutex)
            {
                if (!int.TryParse(inputThreadsAmount.Text, out _threadsAmount))
                {
                    inputThreadsAmount.Foreground = Brushes.Red;
                }
                else
                {
                    inputThreadsAmount.Foreground = Brushes.Black;
                }
            }
        }
    }
}
