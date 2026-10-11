# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0028-20261011-102906)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 305 | 3691055 | 2247168 | 60.9% | 60.9% |
| GPT-6.1 Sol | 245 | 8263242 | 7796992 | 94.4% | 94.7% |
| Sonnet 5.5 | 189 | 3820137 | 3629874 | 95.0% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7567 | 84737515 | 43292672 | 51.1% | 51.0% |
| GPT-6.1 Sol | 6076 | 177489968 | 165411200 | 93.2% | 93.6% |
| Sonnet 5.5 | 6223 | 136836885 | 130634594 | 95.5% | 96.1% |
