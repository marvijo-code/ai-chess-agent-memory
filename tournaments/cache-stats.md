# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 215 | 2109697 | 885248 | 42.0% | 41.7% |
| GPT-6.1 Sol | 240 | 7615968 | 7180672 | 94.3% | 94.9% |
| Sonnet 5.5 | 223 | 5356694 | 5132074 | 95.8% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1394 | 15369591 | 7060736 | 45.9% | 45.9% |
| GPT-6.1 Sol | 1170 | 34838654 | 32595712 | 93.6% | 94.0% |
| Sonnet 5.5 | 1226 | 27989240 | 26795098 | 95.7% | 96.2% |
