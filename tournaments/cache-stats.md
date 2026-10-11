# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 194 | 1941241 | 1089536 | 56.1% | 56.1% |
| GPT-6.1 Sol | 118 | 2435635 | 2171520 | 89.2% | 90.4% |
| Sonnet 5.5 | 127 | 2156726 | 2019818 | 93.7% | 94.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7765 | 86742448 | 44432384 | 51.2% | 51.2% |
| GPT-6.1 Sol | 6194 | 179925603 | 167582720 | 93.1% | 93.6% |
| Sonnet 5.5 | 6353 | 139071272 | 132728888 | 95.4% | 96.1% |
