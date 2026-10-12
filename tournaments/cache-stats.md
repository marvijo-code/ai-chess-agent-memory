# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0033-20261012-032459)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| GPT-6.1 Sol | 129 | 3805804 | 3487488 | 91.6% | 92.7% |
| Sonnet 5.5 | 136 | 3573080 | 3429557 | 96.0% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8542 | 95989801 | 49419264 | 51.5% | 51.4% |
| GPT-6.1 Sol | 6975 | 204188353 | 190066176 | 93.1% | 93.6% |
| Sonnet 5.5 | 7005 | 154969757 | 147911037 | 95.4% | 96.1% |
