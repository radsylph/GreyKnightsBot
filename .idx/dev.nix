

# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [ pkgs.python3 ];
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [ "ms-python.python" ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        install =
          "python -m venv .venv         && source .venv/bin/activate         && pip install -r requirements.txt";
      };
        onStart = {
          install =
          "python -m venv .venv         && source .venv/bin/activate && python main.py";
        };
      # To run something each time the workspace is (re)started, use the `onStart` hook
    };
   
  };
}
