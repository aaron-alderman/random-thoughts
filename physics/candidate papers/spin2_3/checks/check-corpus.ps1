[CmdletBinding()]
param(
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$markdownFiles = Get-ChildItem -Path $repoRoot -Recurse -File -Filter "*.md"

$failed = $false

function Show-Section {
    param(
        [string]$Name,
        [object[]]$Items
    )

    if ($Items.Count -eq 0) {
        if (-not $Quiet) {
            Write-Host "[ok] $Name"
        }
        return
    }

    $script:failed = $true
    Write-Host "[fail] $Name" -ForegroundColor Red
    $Items | Format-Table -AutoSize
}

$stalePatterns = @(
    "0b -",
    "0c -",
    "0d -",
    "0e -",
    "1 - master",
    "2a -",
    "2b -",
    "2c -",
    "2d -",
    "2e -",
    "2f -",
    "2g -",
    "2h -",
    "3- overflow",
    "3c -",
    "3e -",
    "4 - spectral",
    "4a -",
    "next.md",
    "new.md",
    "paper1 - octonionic",
    "paper2 - dIII",
    "all/phase-portrait",
    "C:/Users",
    "C:\Users"
)

$staleMatches = foreach ($file in $markdownFiles) {
    foreach ($match in Select-String -LiteralPath $file.FullName -Pattern $stalePatterns -SimpleMatch) {
        [pscustomobject]@{
            File = $file.FullName.Substring($repoRoot.Length + 1)
            Line = $match.LineNumber
            Text = $match.Line.Trim()
        }
    }
    foreach ($match in Select-String -LiteralPath $file.FullName -Pattern "(?<!faddeev-)efimov[\\/]" -CaseSensitive) {
        [pscustomobject]@{
            File = $file.FullName.Substring($repoRoot.Length + 1)
            Line = $match.LineNumber
            Text = $match.Line.Trim()
        }
    }
}

$overclaimPatterns = @(
    "Gap closed",
    "now a theorem",
    "Casimir in disguise",
    "This closes the speculative bridge",
    "already a theorem"
)

$overclaimMatches = foreach ($file in $markdownFiles) {
    foreach ($match in Select-String -LiteralPath $file.FullName -Pattern $overclaimPatterns -SimpleMatch) {
        [pscustomobject]@{
            File = $file.FullName.Substring($repoRoot.Length + 1)
            Line = $match.LineNumber
            Text = $match.Line.Trim()
        }
    }
}

$badEfimovCoreMatches = foreach ($file in Get-ChildItem -Path (Join-Path $repoRoot "core") -Recurse -File -Filter "*.md") {
    foreach ($match in Select-String -LiteralPath $file.FullName -Pattern "Efimov scaling" -SimpleMatch) {
        if ($match.Line -notmatch "open conjecture|conjectur|speculative") {
            [pscustomobject]@{
                File = $file.FullName.Substring($repoRoot.Length + 1)
                Line = $match.LineNumber
                Text = $match.Line.Trim()
            }
        }
    }
}

$brokenMarkdownRefs = foreach ($file in $markdownFiles) {
    $text = Get-Content -LiteralPath $file.FullName -Raw
    $dir = Split-Path -Parent $file.FullName
    foreach ($match in [regex]::Matches($text, '`([^`]+\.md)`')) {
        $ref = $match.Groups[1].Value
        if ($ref -match "^[A-Za-z]:" -or $ref -match "^https?://") {
            continue
        }

        $relativeCandidate = Join-Path $dir $ref
        $rootCandidate = Join-Path $repoRoot $ref

        if (-not (Test-Path -LiteralPath $relativeCandidate) -and -not (Test-Path -LiteralPath $rootCandidate)) {
            [pscustomobject]@{
                File = $file.FullName.Substring($repoRoot.Length + 1)
                Reference = $ref
            }
        }
    }
}

Show-Section "stale flat-corpus references" @($staleMatches)
Show-Section "retired bridge overclaim phrases" @($overclaimMatches)
Show-Section "unqualified core Efimov scaling references" @($badEfimovCoreMatches)
Show-Section "broken backticked markdown references" @($brokenMarkdownRefs)

if ($failed) {
    exit 1
}

if (-not $Quiet) {
    Write-Host "Corpus checks passed." -ForegroundColor Green
}
