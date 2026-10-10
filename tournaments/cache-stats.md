# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 85 | 840802 | 348672 | 41.5% | 41.2% |
| GPT-6.1 Sol | 68 | 1575322 | 1440768 | 91.5% | 92.4% |
| Sonnet 5.5 | 83 | 1872453 | 1795169 | 95.9% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4587 | 50368238 | 24030848 | 47.7% | 47.6% |
| GPT-6.1 Sol | 3737 | 106940539 | 99215104 | 92.8% | 93.3% |
| Sonnet 5.5 | 3980 | 87642811 | 83695917 | 95.5% | 96.1% |
