# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 180 | 1715425 | 737664 | 43.0% | 42.8% |
| GPT-6.1 Sol | 222 | 7192340 | 6776576 | 94.2% | 94.9% |
| Sonnet 5.5 | 223 | 5356694 | 5132074 | 95.8% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1359 | 14975319 | 6913152 | 46.2% | 46.1% |
| GPT-6.1 Sol | 1152 | 34415026 | 32191616 | 93.5% | 94.0% |
| Sonnet 5.5 | 1226 | 27989240 | 26795098 | 95.7% | 96.2% |
