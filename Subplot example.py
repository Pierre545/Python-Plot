a_crop_original = Lhasa_MNDWI_true[176:276,59:184]
a_skel = ski.skeletonize(sobel)
a_axis = ski.medial_axis(sobel)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
fig.suptitle('DGO_23', fontsize=20)
ax1.set_title('Image originale')
ax1.imshow(a_crop_original, cmap="gray")

ax2.set_title("Sobel gradient")
ax2.imshow(sobel[176:276,59:184], cmap="gray")
ax2.yaxis.set_visible(False)

ax3.set_title("Medial axis crop")
ax3.imshow(a_axis[176:276,59:184], cmap="gray")
ax3.yaxis.set_visible(False)

ax4.set_title("Skeletonize crop")
ax4.imshow(a_skel, cmap="gray")
ax4.yaxis.set_visible(False)

plt.tight_layout()
plt.show()
