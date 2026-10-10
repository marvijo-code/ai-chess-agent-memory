# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 78 | 697058 | 371328 | 53.3% | 52.7% |
| GPT-6.1 Sol | 48 | 906380 | 803840 | 88.7% | 90.4% |
| Sonnet 5.5 | 76 | 1529565 | 1456737 | 95.2% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5157 | 56384044 | 26849280 | 47.6% | 47.5% |
| GPT-6.1 Sol | 4170 | 120335709 | 111739008 | 92.9% | 93.3% |
| Sonnet 5.5 | 4425 | 97476680 | 93093040 | 95.5% | 96.1% |
