# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 162 | 2466184 | 1332224 | 54.0% | 54.0% |
| GPT-6.1 Sol | 47 | 855263 | 795648 | 93.0% | 93.8% |
| Sonnet 5.5 | 86 | 1800720 | 1719502 | 95.5% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6625 | 74362783 | 37413376 | 50.3% | 50.3% |
| GPT-6.1 Sol | 5243 | 151128687 | 140638336 | 93.1% | 93.5% |
| Sonnet 5.5 | 5530 | 122074149 | 116575531 | 95.5% | 96.1% |
