# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0026-20261011-055315)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 158 | 1651878 | 908288 | 55.0% | 55.0% |
| GPT-6.1 Sol | 80 | 1633956 | 1502080 | 91.9% | 92.8% |
| Sonnet 5.5 | 108 | 2543160 | 2430843 | 95.6% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6930 | 77485457 | 39072256 | 50.4% | 50.4% |
| GPT-6.1 Sol | 5432 | 155467069 | 144674816 | 93.1% | 93.5% |
| Sonnet 5.5 | 5759 | 127151341 | 121416652 | 95.5% | 96.1% |
