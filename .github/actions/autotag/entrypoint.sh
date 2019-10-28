#!/bin/bash
set eox

# get latest tag
# you need at least one tag in repo
old_tag=$(git describe --tags `git rev-list --tags --max-count=1`)
tag_commit=$(git rev-list -n 1 $old_tag)

# get current commit hash for tag
commit=$(git rev-parse HEAD)

if [ "$tag_commit" == "$commit" ]; then
    echo "No new commits since previous tag. Skipping ..."
    exit 0
fi

# get new tag
new_tag=$(echo $old_tag | python /get_new_tag.py)

echo "Pushing tag $new_tag to repo ..."
git_refs_url=$(jq .repository.git_refs_url $GITHUB_EVENT_PATH | tr -d '"' | sed 's/{\/sha}//g')

curl -s -X POST $git_refs_url \
-H "Authorization: token $GITHUB_TOKEN" \
-d @- << EOF
{
  "ref": "refs/tags/$new_tag",
  "sha": "$commit"
}
EOF
