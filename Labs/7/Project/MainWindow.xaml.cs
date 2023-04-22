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
            _gameLife.RandomFilling();

            _gameSimulationTask = Task.Run(async () =>
            {
                while (true)
                {
                    if (_isSimulationAlive)
                    {
                        _gameLife.Move();

                        await Task.Delay(600);
                    }
                }
            });
        }

        private const int GameSize = 20;

        private GameLife _gameLife = new GameLife(GameSize);
        private Bitmap _mainViewBuffer = new Bitmap(GameSize, GameSize);

        private readonly Task _gameSimulationTask;
        private bool _isSimulationAlive = false;

        /// <summary>
        /// Convert Bitmap to ImageSource <b> [Not Mine] </b>
        /// </summary>
        /// <param name="bitmap"> Bitmap that will be converted </param>
        /// <returns> Converted Bitmap as ImageSource </returns>
        private ImageSource BitmapToImageSource(Bitmap bitmap)
        {
            MemoryStream ms = new MemoryStream();
            bitmap.Save(ms, System.Drawing.Imaging.ImageFormat.Bmp);
            BitmapImage image = new BitmapImage();
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
        private void RedrawImage(List<(int x, int y, bool newCellValue)> changes)
        {
            var liveCellColor = Color.White;
            var deadCellColor = Color.Black;

            foreach (var change in changes)
            {
                _mainViewBuffer.SetPixel(change.x, change.y,
                    change.newCellValue ? liveCellColor : deadCellColor);
            }

            mainView.Source = BitmapToImageSource(_mainViewBuffer);
        }

    }
}