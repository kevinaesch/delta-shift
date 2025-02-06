{
  description = "A dev shell with python312Packages.yfinance, poetry, neovim, and python312Packages.numpy";

  inputs = {
    # Use the unstable channel, which tends to have the latest packages.
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.python312Packages.yfinance
            pkgs.poetry
            pkgs.neovim
            pkgs.python312Packages.numpy
          ];
        };
      }
    );
}

