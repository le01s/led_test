# LED Strip Control with `main.py`

This Python script controls an LED strip using the `rpi_ws281x` library, which is commonly used for controlling WS2812B (NeoPixel) LED strips on Raspberry Pi. The script provides several animation modes, including a snake effect, full-color display, odd/even pixel coloring, and multiple snakes moving simultaneously.

## Requirements

1. **Hardware**:
   - Raspberry Pi (any model with GPIO pins).
   - WS2812B (NeoPixel) LED strip.
   - Proper wiring between the Raspberry Pi and the LED strip (ensure correct voltage levels and current capacity).

2. **Software**:
   - Python 3.x.
   - `rpi_ws281x` library installed. You can install it using pip:
     ```bash
     pip install rpi_ws281x
     ```
   - Ensure the Raspberry Pi is configured to allow GPIO access.

## Configuration

Before running the script, ensure the following constants are set correctly in the `main.py` file:

- `LED_COUNT`: The number of LEDs in your strip.
- `LED_PIN`: The GPIO pin connected to the LED strip (default is 18).
- `LED_FREQ_HZ`: Frequency of the signal (usually 800000 Hz).
- `LED_DMA`: DMA channel (usually 10).
- `LED_INVERT`: Set to `True` if using an NPN transistor for signal inversion.
- `LED_CHANNEL`: Set to `0` for GPIO 18, or `1` for GPIO 13, 19, 41, 45, or 53.

## Usage

Run the script using Python 3:

```bash
python3 main.py
```
After running the script, you will be prompted to select an animation mode by entering a number:

1. **Snake with Fade**:
    - A single snake moves along the LED strip with a fading tail.
    - The brightness gradually increases until it reaches maximum.

2. **Full Color with Changing Brightness**:
   - The entire LED strip displays a single color (green by default).
   - The brightness oscillates between 30 and 120.

3. **Odd/Even Pixel Coloring**:
   - Alternates colors between odd and even pixels.
   - Colors are randomly generated for each iteration.

4. **Multiple Snakes with Fade**:
   - Multiple snakes move along the LED strip simultaneously.
   - Each snake has a fading tail, and the colors are randomly generated.

5. **Invalid Input**:
   - If an invalid number is entered, the LED strip will display a solid green color for 5 seconds before exiting.

## Exiting the Script

To exit the script, press `Ctrl+C`. This will turn off all LEDs and reset the strip.

## Functions

### `snakeWithFade(strip, color, wait_ms=50, tail_length=10, br=255)`
- Animates a single snake moving along the strip with a fading tail.
- Parameters:
  - `strip`: The LED strip object.
  - `color`: The color of the snake.
  - `wait_ms`: Delay between each step (in milliseconds).
  - `tail_length`: Length of the fading tail.
  - `br`: Brightness of the LEDs.

### `manySnakesWithFade(strip, color, wait_ms=50, tail_length=10, br=255, gap=10)`
- Animates multiple snakes moving along the strip simultaneously.
- Parameters:
  - `strip`: The LED strip object.
  - `color`: The color of the snakes.
  - `wait_ms`: Delay between each step (in milliseconds).
  - `tail_length`: Length of the fading tail.
  - `br`: Brightness of the LEDs.
  - `gap`: Distance between each snake.

### `fullColor(strip, color, wait_ms=50, br=255)`
- Fills the entire LED strip with a single color.
- Parameters:
  - `strip`: The LED strip object.
  - `color`: The color to fill the strip.
  - `wait_ms`: Delay after setting the color (in milliseconds).
  - `br`: Brightness of the LEDs.

### `oddPixels(strip, color_odd, color_non_odd, wait_ms=50, br=255)`
- Alternates colors between odd and even pixels.
- Parameters:
  - `strip`: The LED strip object.
  - `color_odd`: Color for odd-numbered pixels.
  - `color_non_odd`: Color for even-numbered pixels.
  - `wait_ms`: Delay after setting the colors (in milliseconds).
  - `br`: Brightness of the LEDs.

### `rand_number()`
- Generates a random number between 1 and 255.
- Used for generating random colors.

## Notes

- Ensure the Raspberry Pi has sufficient power to drive the LED strip. Use an external power supply if necessary.
- Adjust the `LED_COUNT` and `LED_PIN` values according to your setup.
- The script is designed to run indefinitely in most modes. Use `Ctrl+C` to stop it.

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

---

Enjoy creating mesmerizing LED animations with your Raspberry Pi! 🎉