{
  description = "A dev shell with yfinance, poetry, neovim, numpy and a Docker image build";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        # The development shell with the required packages
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.python312Packages.yfinance
            pkgs.poetry
            pkgs.neovim
            pkgs.python312Packages.numpy
          ];
        };

        # Build a Docker image only on x86_64-linux.
        # For non-linux systems, you might consider overriding the system.
        dockerImage = if system == "x86_64-linux" then pkgs.dockerTools.buildImage {
          name = "my-docker-image";
          tag = "latest";
          # The 'contents' attribute specifies what is included in the image.
          # In this example, we include the same packages as in the devShell.
          contents = [
            pkgs.python312Packages.yfinance
            pkgs.poetry
            pkgs.neovim
            pkgs.python312Packages.numpy
          ];
          # Configure the image. Here we set the default command to a shell.
          config = {
            Cmd = [ "/bin/sh" ];
          };
        } else null;
      }
    );
}

