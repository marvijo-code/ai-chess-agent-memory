# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0028-20261011-102906)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 23 | 188573 | 98816 | 52.4% | 52.0% |
| GPT-6.1 Sol | 16 | 243141 | 227328 | 93.5% | 95.1% |
| Sonnet 5.5 | 21 | 265759 | 242391 | 91.2% | 93.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7285 | 81235033 | 41144320 | 50.6% | 50.6% |
| GPT-6.1 Sol | 5847 | 169469867 | 157841536 | 93.1% | 93.6% |
| Sonnet 5.5 | 6055 | 133282507 | 127247111 | 95.5% | 96.1% |
