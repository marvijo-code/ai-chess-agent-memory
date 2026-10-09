# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 125 | 1327925 | 551552 | 41.5% | 41.3% |
| GPT-6.1 Sol | 101 | 2523515 | 2283904 | 90.5% | 91.4% |
| Sonnet 5.5 | 117 | 2263795 | 2140306 | 94.5% | 95.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1829 | 20407459 | 9385728 | 46.0% | 45.9% |
| GPT-6.1 Sol | 1475 | 42790214 | 39883264 | 93.2% | 93.7% |
| Sonnet 5.5 | 1659 | 38063997 | 36433917 | 95.7% | 96.2% |
