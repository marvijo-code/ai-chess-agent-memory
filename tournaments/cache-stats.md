# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 99 | 1014608 | 551424 | 54.3% | 54.3% |
| GPT-6.1 Sol | 79 | 2338675 | 2179584 | 93.2% | 93.5% |
| Sonnet 5.5 | 53 | 777206 | 717940 | 92.4% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6287 | 69850739 | 34825728 | 49.9% | 49.8% |
| GPT-6.1 Sol | 5061 | 145854497 | 135676928 | 93.0% | 93.5% |
| Sonnet 5.5 | 5297 | 116830419 | 111558848 | 95.5% | 96.1% |
