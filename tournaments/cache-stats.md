# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0030-20261011-145519)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 84 | 741526 | 322048 | 43.4% | 43.0% |
| GPT-6.1 Sol | 121 | 4383108 | 4099328 | 93.5% | 93.8% |
| Sonnet 5.5 | 84 | 2002418 | 1919264 | 95.8% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7908 | 88127893 | 45112320 | 51.2% | 51.1% |
| GPT-6.1 Sol | 6347 | 185007707 | 172301696 | 93.1% | 93.6% |
| Sonnet 5.5 | 6459 | 141364498 | 134914714 | 95.4% | 96.1% |
