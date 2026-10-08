# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 288 | 3365217 | 1630592 | 48.5% | 48.4% |
| GPT-6.1 Sol | 222 | 6805875 | 6276096 | 92.2% | 92.6% |
| Sonnet 5.5 | 212 | 4534199 | 4317530 | 95.2% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1179 | 13259894 | 6175488 | 46.6% | 46.5% |
| GPT-6.1 Sol | 930 | 27222686 | 25415040 | 93.4% | 93.7% |
| Sonnet 5.5 | 1003 | 22632546 | 21663024 | 95.7% | 96.2% |
