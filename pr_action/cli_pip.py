from pr_action import cli
from pr_action.config_loader import get_settings


def main():
    # Fill in the following values
    provider = "github"  # GitHub provider
    user_token = "..."  # GitHub user token
    openai_key = "ghs_afsdfasdfsdf"  # Example OpenAI key
    pr_url = "..."  # PR URL, for example 'https://github.com/Pr-action/pr-action/pull/809'
    command = "/improve"  # Command to run (e.g. '/review', '/describe', 'improve', '/ask="What is the purpose of this PR?"')

    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    output = cli.run_command(pr_url, command)

    print(output)

if __name__ == '__main__':
    main()
