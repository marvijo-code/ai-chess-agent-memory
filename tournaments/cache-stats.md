# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0033-20261012-032459)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| GPT-6.1 Sol | 92 | 2883721 | 2672128 | 92.7% | 93.3% |
| Sonnet 5.5 | 48 | 1275060 | 1225723 | 96.1% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8542 | 95989801 | 49419264 | 51.5% | 51.4% |
| GPT-6.1 Sol | 6938 | 203266270 | 189250816 | 93.1% | 93.6% |
| Sonnet 5.5 | 6917 | 152671737 | 145707203 | 95.4% | 96.1% |
